def isFull(Stack,top,N):
    if top==N-1: #如果top指標指向堆疊頂端,傳回True
        return True
    else: #否則傳回False
        return False

def isEmpty(stack,top):
    if top==-1: #如果top指標為-1,傳回True
        return True
    else: #否則傳回False
        return False