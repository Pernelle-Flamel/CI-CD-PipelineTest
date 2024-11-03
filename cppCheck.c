void printArray(int *arr, int size) {
    for (int i = 0; i <= size; i++) {  // Fehler: Array-Out-of-Bounds
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void memoryLeakExample() {
    int *leakedMemory = (int*)malloc(10 * sizeof(int));  // Fehler: Speicherleck
    // 'leakedMemory' wird nicht freigegeben
}

void nullPointerDereference() {
    int *ptr = NULL;
    *ptr = 5;  // Fehler: Dereferenzierung eines Null-Pointers
}

int uninitializedVariableExample() {
    int x;  // Fehler: uninitialisierte Variable
    return x + 1;
}

int main() {
    int unusedVar = 10;  // Fehler: Nicht verwendete Variable

    int array[5] = {1, 2, 3, 4, 5};
    printArray(array, 5);  // Fehler: Übergabe falscher Array-Größe

    memoryLeakExample();
    nullPointerDereference();
    uninitializedVariableExample();

    while (1) {  // Warnung: Endlosschleife
        // Schleifeninhalt fehlt
    }

    return 0;
}
