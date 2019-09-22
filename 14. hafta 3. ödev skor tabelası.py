import os

#alicenin PUANLARI KÜÇÜKTEN BÜYÜĞE SIRALI
##BU SEBEPLE DÜŞÜK SIRADAN BAŞLAMALI ARAMAYA.. DİĞER YANDAN DAHA SONRAKİ DERECELERDE BAKILAN YERLERE BİR DAHA BAKMAMALI


def climbingLeaderboard(scores, alice):
    
    score_k=sorted(list(set(scores)))[::-1]
    
    def bak(i):
        for k in score_k:
            if i >=k:
                return score_k.index(k)+1
        if i<score_k[-1]:
            return len(score_k)+1
    return list(map(bak,alice))

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
