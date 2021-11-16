import torch
import urllib.request
import pandas as pd
from torchtext import data # torchtext.data 임포트
from konlpy.tag import Mecab
import torch.nn as nn

class KoreanTorch:
    def __init__(self):
        pass

    def my_mecab(self):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt",
                                   filename="data/ratings_train.txt")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt",
                                   filename="data/ratings_test.txt")

        train_df = pd.read_table('data/ratings_train.txt')
        test_df = pd.read_table('data/ratings_test.txt')

        print(f'메캅 상위 5 {train_df.head(5)}')
        print(f'훈련 데이터 샘플의 개수 : {len(train_df)}')
        print(f'테스트 데이터 샘플의 개수 : {len(test_df)}')
        print('************************ 1 ********************************')

        tokenizer = Mecab()

        # 필드 정의
        ID = data.Field(sequential=False,
                        use_vocab=False)  # 실제 사용은 하지 않을 예정

        TEXT = data.Field(sequential=True,
                          use_vocab=True,
                          tokenize=tokenizer.morphs,  # 토크나이저로는 Mecab 사용.
                          lower=True,
                          batch_first=True,
                          fix_length=20)

        LABEL = data.Field(sequential=False,
                           use_vocab=False,
                           is_target=True)

        train_data, test_data = data.TabularDataset.splits(
            path='.', train='ratings_train.txt', test='ratings_test.txt', format='tsv',
            fields=[('id', ID), ('text', TEXT), ('label', LABEL)], skip_header=True)

        print('훈련 샘플의 개수 : {}'.format(len(train_data)))
        print('테스트 샘플의 개수 : {}'.format(len(test_data)))

        print(vars(train_data[0]))

        print('************************ 5. 단어 집합(Vocabulary) 만들기 ********************************')

        TEXT.build_vocab(train_data, min_freq=10, max_size=10000)

        print('단어 집합의 크기 : {}'.format(len(TEXT.vocab)))

        print(TEXT.vocab.stoi)

        print('************************ 토치텍스트의 데이터로더 만들기 ********************************')

        batch_size = 5
        train_loader = data.Iterator(dataset=train_data, batch_size=batch_size)
        test_loader = data.Iterator(dataset=test_data, batch_size=batch_size)

        print('훈련 데이터의 미니 배치 수 : {}'.format(len(train_loader)))
        print('테스트 데이터의 미니 배치 수 : {}'.format(len(test_loader)))

        batch = next(iter(train_loader))  # 첫번째 미니배치
        print(batch.text)

        '''
        배치 크기가 5이기 때문에 5개의 샘플이 출력되는 것을 볼 수 있습니다. 
        각 샘플의 길이는 20의 길이를 가지는데, 
        이는 앞서 초기에 필드를 정의할 때 fix_length를 20으로 정해주었기 때문입니다. 
        다시 말해 하나의 미니 배치의 크기는 (배치 크기 × fix_length)입니다.
        샘플의 중간, 중간에는 숫자 0이 존재하는데 이는 단어 집합에 포함되지 못한 단어들은 
        <unk>라는 토큰으로 변환되었음을 의미합니다. 
        또한 기존 샘플 길이가 20보다 작았던 샘플들은 뒤에 <pad> 토큰의 번호인 숫자 1로 패딩되었습니다.
        
        '''


class EnglishTorch:
    def __init__(self):
        pass

    def execute(self):
        train_data = 'you need to know how to code'
        word_set = set(train_data.split())  # 중복을 제거한 단어들의 집합인 단어 집합 생성.
        vocab = {word: i + 2 for i, word in enumerate(word_set)}  # 단어 집합의 각 단어에 고유한 정수 맵핑.
        vocab['<unk>'] = 0
        vocab['<pad>'] = 1
        print(vocab)

        # 단어 집합의 크기만큼의 행을 가지는 테이블 생성.
        embedding_table = torch.FloatTensor([
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.2, 0.9, 0.3],
            [0.1, 0.5, 0.7],
            [0.2, 0.1, 0.8],
            [0.4, 0.1, 0.1],
            [0.1, 0.8, 0.9],
            [0.6, 0.1, 0.1]])

        # 임의의 샘플 문장
        sample = 'you need to run'.split()
        idxes = []
        # 각 단어를 정수로 변환
        for word in sample:
            try:
                idxes.append(vocab[word])
            except KeyError:  # 단어 집합에 없는 단어일 경우 <unk>로 대체된다.
                idxes.append(vocab['<unk>'])
        idxes = torch.LongTensor(idxes)

        # 룩업 테이블
        lookup_result = embedding_table[idxes, :]  # 각 정수를 인덱스로 임베딩 테이블에서 값을 가져온다.
        print(lookup_result)
        '''
        결과: tensor([[0.1000, 0.5000, 0.7000],
                [0.1000, 0.8000, 0.9000],
                [0.4000, 0.1000, 0.1000],
                [0.0000, 0.0000, 0.0000]])'''

        # 2. 임베딩 층 사용하기

        train_data = 'you need to know how to code'
        word_set = set(train_data.split())  # 중복을 제거한 단어들의 집합인 단어 집합 생성.
        vocab = {tkn: i + 2 for i, tkn in enumerate(word_set)}  # 단어 집합의 각 단어에 고유한 정수 맵핑.
        vocab['<unk>'] = 0
        vocab['<pad>'] = 1

        embedding_layer = nn.Embedding(num_embeddings=len(vocab),
                                       embedding_dim=3,
                                       padding_idx=1)
        print(embedding_layer.weight)
        '''
        Parameter containing:
            tensor([[-0.1778, -1.9974, -1.2478],
                    [ 0.0000,  0.0000,  0.0000],
                    [ 1.0921,  0.0416, -0.7896],
                    [ 0.0960, -0.6029,  0.3721],
                    [ 0.2780, -0.4300, -1.9770],
                    [ 0.0727,  0.5782, -3.2617],
                    [-0.0173, -0.7092,  0.9121],
                    [-0.4817, -1.1222,  2.2774]], requires_grad=True)
        '''


if __name__ == '__main__':
    # https://wikidocs.net/64904
    print(f'Result: {torch.cuda.is_available()}')
    # k = KoreanTorch()
    # k.my_mecab()
    e = EnglishTorch()
    e.execute()