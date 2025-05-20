def radix_sort(arr):

    # Randame didziausia skaiciu ir nustatome kiek skaitmenu jis turi
    max_val = max(arr)
    exp = 1 # Pradedam nuo vienetu

    while max_val // exp > 0:
        # Sukuriame 10 "buckets" skaiciams nuo 0 iki 9
        buckets = [[] for _ in range(10)]

        # Kiekviena elementa priskiriame atitinkamam "bucket"
        for number in arr:
            index = (number // exp) % 10
            buckets[index].append(number)

        # Sujungiame "buckets" atgal į vieną sarasa
        arr = [num for bucket in buckets for num in bucket]

        exp *= 10

    return arr

def main():
    skaiciai = [170, 956, 75, 90, 802, 24, 66, 66, 9999, 100]
    print(radix_sort(skaiciai))

if __name__ == "__main__":
    main()
