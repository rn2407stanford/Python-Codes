# autograde:all-correct a11111111 time:2022-10-26T19:03:22+00:00 UTC
def at_swap(s):
    """
    We are first finding @@@ with the command find,
    then defining the start part that we need and the end part
    then summing it and returning what we have.
    """
    if s.find("@@@")!= -1:
            at_index=s.find('@@@')
            start = s[: at_index]
            end= s[at_index+3:]
            all=end+start
            return all
    return ''
    
        
