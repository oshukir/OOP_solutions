def show_me(instance):
    attrs = sorted(instance.__dict__.keys())
    name = instance.__class__.__name__
    
    first_s = f"Hi, I'm one of those {name}s! "
    second_s = "Have a look at my "
    
    if len(attrs) > 1:
        last_is_out = ", ".join(attrs[:len(attrs)-1])
        second_s += last_is_out + " and " + attrs[-1] + "."
    else:
        second_s += attrs[-1] + "."
        
    return first_s + second_s