#Q8. Flip a dictionary. Given {"a": 1, "b": 2, "c": 3}, create a new dictionary {1: "a", 2: "b", 3: "c"}.
original_dict = {"a": 1, "b": 2, "c": 3}
flipped_dict = {v: k for k, v in original_dict.items()}
print(flipped_dict)