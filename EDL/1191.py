def organize(inorder, index):
    global postorder
    global preorder
    if not preorder or not inorder:
        return
    postorder = preorder[index] + postorder
    left, right = inorder.split(preorder[index])

    preorder = preorder.replace(preorder[index], '')
    if right and preorder:
        for elem in preorder:
            if elem in right:
                nx = elem
                break
        organize(right, preorder.index(nx))
    if left and preorder:
        for elem in preorder:
            if elem in left:
                nx = elem
                break
        organize(left, preorder.index(nx))


while True:
    postorder = ""
    try:
        inp = input()
    except (EOFError):
        break
    preorder, inorder = inp.split()
    organize(inorder, 0)
    print (postorder)
