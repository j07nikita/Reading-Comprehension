from drqa.tokenizers import CoreNLPTokenizer
tok = CoreNLPTokenizer()
print(tok.tokenize('hello world').words()) 