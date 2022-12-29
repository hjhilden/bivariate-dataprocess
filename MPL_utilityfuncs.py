from math import ceil, sqrt

def squared(value):
    return ceil(sqrt(value))


def cm2inch(*tupl):
    """Convert centimeters to inches.
    Args:
        tupl: value or pair of values to convert
    """
    inch = 2.54000508001
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        if len(tupl)==1:
            return tupl[0]/inch
        else:
            return tuple(i/inch for i in tupl)


# improved make margins
def make_margins(width, height, margins=None, left=0, right=0, top=0, bottom=0):
    """Create Matplotlib margins. Returns tuple that can be unpacked for adjust_subplots with *
    Args:
        width, height: figure size
        margins: equal margins all around
        left, right, top, bottom: set individual margins
    """
    if margins: 
        left = margins
        right = margins
        top = margins
        bottom = margins

    LM = left/width
    BM = bottom/height
    RM = 1-right/width
    TM = 1-top/height
    return LM, BM, RM, TM

def format_with_unit(val, precision=1, suffix="%"):
    d = '{:.{prec}f}{suffix}'.format(val, prec=precision, suffix="%")
    return d

def format_signed_unicode(val, precision=2):
    d = '{:{sign}.{prec}f}'.format(val, sign='+', prec=precision)
    if abs(val) == 0.0: d = d.replace('+', '')
    d = d.replace('-', '−') # unicode minus
    return d


# MATPLOTLIB func formatters

def format_percentage_nodecimals_eng(axis, pos):
    # multiplied *100, percentage sign, english formatting, no decimals
    axis*=100
    return ('%.0f%%' % axis)

# Func formatter - finnish decimals
def format_decimalcomma_fi(axis, pos):
    return ('%.2f' % axis).replace('.', ',')

# Func formatter - decimals
def format_decimals(axis, pos):
    return ('%.1f' % axis)

# Func formatter finnish decimals show plus-minus
def format_decimalcomma_signed(axis, pos):
    d = '{:{sign}.{prec}f}'.format(axis, sign='+', prec=0)
    if abs(axis) == 0.0: d = d.replace('+', '')
    return d.replace('.', ',')

# Func formatter show plus-minus
def format_decimals_signed(axis, pos):
    d = '{:{sign}.{prec}f}'.format(axis, sign='+', prec=1)
    if abs(axis) == 0.0: d = d.replace('+', '')
    return d

# Func formatter thousands
def format_thousands(value, tick):
    return '{:,.0f}'.format(value)
