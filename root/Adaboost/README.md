---
sort: 1
---
# Adaboost
Adaboost 는 Adaptive Boosting의 약자이다.   
`Machine learning meta-algorithm`으로 다른 learning algorithm과 함께 사용하여 성능향상을 할 수 있다.  
여러 model을 enssenble하여 성능 boosting을 한다.  
각 model의 성능이 약하더라도 enssenble하면 향상된다.    
이런 의미에서 각 하나의 model을 `weak model`로 부른다.   
학습은 model 하나씩 순차적으로 학습해나가는 방식이다.  
총 모델들를 학습하는 횟수를 `Round`라고 한다. 
총 T 개의 model을 학습한다고 하면 $M_t \ , t=1,\dots, T$ 으로 표현 할 수 있다.   
T 개의 Round를 거쳐서 학습한다고 바꿔 말할수있다.   
$M_t$를 학습 할때 한 스텝 이전 모델 $M_{t-1}$ 이 잘못 예측한 데이터를 더 집중해서 학습하여 보완한다.    
이때 데이터의 총 개수가 N개라면 $x_i \ ,i=1,\dots, N$으로 표현할 수있다.    
그리고 $t$번째 Round에서 $i$ 번째 데이터의 중요도를 $D_i^t$ 로 표현 할 수있다.  
다음 Round로 넘어갈때 $D_i^t$는 $D_i^{t+1}$로 업데이트 된다.    
잘못 예측된 데이터에 대해서는 가중치를 높이고 잘 예측된 데이터에 대해서는 가중치를 낮춘다.  
Adaboost는 데이터에만 가중치를 계산하는것이 아니라 $model_t$에도 모델의 중요도를 계산한다.  
$t$번째 모델의 중요도를 $W_t$라고 한다면 최종적으로 예측하는 결과 값은 $y = \sum_{t=1}^T W_tM_t(x)$로 계산된다. 

## Random performance model
여러 model을 enssenble하기때문에 각 model의 성능이 좋을 수록 최종 model은 더 좋은 값을 예측할 것이다.  Adaboost에서 최악의 경우는 weak model이 random 하게 예측하는 성능을 내는것이다. Random performance model 이 경우 essemble해서 성능 개선이 없다. 다시 잘 생각해보면 다음 Round에서 집중해서 학습할 데이터가 랜덤하게 선택되는것이기 때문에 잘못된것을 보완하려고 했지만 사실 잘 못된게 아니여서 그렇다. 만약 weak model의 성능이 random 보다 안좋다면 어떻게 될까? 이 경우는 오히려 이득이 된다. 왜냐하면 결과를 반대로 받아드리면 잘못된 예측은 바른 예측으로 해석 할 수 있기 때문이다.
결론적으로 random 예측에서 멀게 맞게 예측하던지 틀리게 예측하는 모델이 더 좋은 weak model이 된다.

