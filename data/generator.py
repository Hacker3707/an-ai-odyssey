import json
import os
import random

def generate_knapsack_dataset(n_items, correlation="uncorrelated", r_max=100, seed=42):
    """
    Sinh bộ dữ liệu 0/1 Knapsack theo chuẩn Pisinger.
    correlation: 'uncorrelated' | 'weakly_correlated' | 'strongly_correlated'
    """
    random.seed(seed + n_items)
    items = []
    
    for i in range(1, n_items + 1):
        w = random.randint(1, r_max)
        
        if correlation == "uncorrelated":
            v = random.randint(1, r_max)
        elif correlation == "weakly_correlated":
            delta = r_max // 10
            v = random.randint(max(1, w - delta), w + delta)
        elif correlation == "strongly_correlated":
            delta = r_max // 10
            v = w + delta
        else:
            raise ValueError("Loại tương quan không hợp lệ!")
            
        items.append({"id": i, "weight": w, "value": v})
        
    total_weight = sum(item["weight"] for item in items)
    capacity = int(0.5 * total_weight)
    
    return {
        "name": f"knapsack_n{n_items}_{correlation}",
        "type": correlation,
        "n_items": n_items,
        "capacity": capacity,
        "items": items
    }

def build_all_datasets(output_dir="data/datasets"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Các kịch bản thực nghiệm cho Chương 3
    sizes = [15, 25, 35, 50, 100, 200, 500]
    correlations = ["uncorrelated", "weakly_correlated", "strongly_correlated"]
    
    for n in sizes:
        for corr in correlations:
            data = generate_knapsack_dataset(n_items=n, correlation=corr)
            file_path = os.path.join(output_dir, f"{data['name']}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                
    print(f"Đã sinh thành công {len(sizes) * len(correlations)} bộ dữ liệu chuẩn tại '{output_dir}/'")

if __name__ == "__main__":
    build_all_datasets()