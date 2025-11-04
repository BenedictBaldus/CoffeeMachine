# binary_search_tree.py

class Node:
    
    def __init__(self, wert):
        self.wert = wert   # Der im Knoten gespeicherte Wert
        self.left = None # Verweis auf den linken Kindknoten
        self.right = None # Verweis auf den rechten Kindknoten


def einfuegen_einzelwert(root, wert):
    
    if root is None:
        return Node(wert)
        
   
    if wert < root.wert:
       
        root.left = einfuegen_einzelwert(root.left, wert)
        
    else:
        root.right = einfuegen_einzelwert(root.right, wert)
        
    return root


def einfuegen_liste(root, wert_liste):
    print(f"Füge die folgende Liste in den Baum ein: {wert_liste}")
    
    for wert in wert_liste:
        root = einfuegen_einzelwert(root, wert)
        
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        
        print(root.wert, end=" ") # 'end=" "' sorgt für Ausgabe in einer Zeile
        
        inorder_traversal(root.right)

# AUSFÜHRUNG

if __name__ == "__main__":

    
    bst_root = None
    
    meine_werte = [35, 17, 88 ,93, 91, 12, 8, 47, 58, 32, 1, 69, 62, 74, 99, 23, 18, 11]
    
    bst_root = einfuegen_liste(bst_root, meine_werte)
    
    print("\nBaum erfolgreich erstellt.")
    
    print("In-order Traversal (sollte sortiert sein):")
    inorder_traversal(bst_root)
    print() 



