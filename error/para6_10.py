import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warnig, no code", SyntaxWarning)
warnings.warn("Warnig, module not import", ImportWarning)