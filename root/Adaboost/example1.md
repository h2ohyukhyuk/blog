---
sort: 1
---

# example1
## Binay Classification

  - Training set    
  \\( h \\)차원 학습데이터 \\( x \\)이 N개 주워졌고 각 데이터에 레이블 \\( y \\) 또한 N개 주워졌다. 레이블이 1 또는 -1 값을 가지는 이진분류 문제이다.
  
  $$ (x_i,y_i) \ where \ i=1,\dots,N
  \newline  \ x_i \in \R^h, y_i \in Y = \{-1, 1\}$$ 

  - Data weight    
  각 학습데이터마다 중요도를 나타내는 가중치\\( D_i \\)가 있고, 이 가중치는 매 round마다 갱신되며 최대 T번 round가 진행된다. 초기 \\( t=1 \\) 에서 초기값은 \\( \frac{1}{N} \\)로 초기화된다.
  $$
  D_i^t \ where \  i=1,\dots,N \ t=1,\dots,T
  \newline 
  D_i^1=\frac{1}{N}
  $$

  - Model
    - Weak model    
    h 차원의 hyperplane으로 분류 하는 선형 모델로 표현했다. \\( sign\\) 함수는 입력값의 부호만 반환하여 0인 경우 0을 반환한다.
      $$\widehat y = M_t(x_i) = sign(w_1*_1x_i+\dots+ w_h*_hx_i+ bias)$$
    - final model
    $$ \widehat y = F(x) =sign(\sum_{t=1}^T{\alpha_t M_t(x)})$$

    - Model error   
    모델 에러 \\( \varepsilon_t \\)는 모델이 잘못 예측한 학습데이터의 가중치를 합한것이다. 모든 데이터에 대해서 다 틀린경우 1이되고, 다 맞힌경우 0이된다.
    $$ \varepsilon_t = \sum_i^N D_i^tI(y_i \neq M_t(x_i)), \ where \ I(true)=1, \ I(flase) = 0 $$

## Model Weight
모델 가중치 \\(\alpha_t\\)는 수식(1)과 같이 모델 에러 \\(\epsilon_t\\)로부터 계산된다. 그래프로 그려보면 Figure.1과 같다. 만약 \(\epsilon_t\)가 0.5라면 \\(\alpha_t\\) 가 0이 되어서 해당 모델이 쓸모없다는것을 알수 있다. 반면 \\(\epsilon_t\\) 가 0과 1에 근접했을때 \\(\alpha_t\\)가 급격하게 각각 증가,감소하여 예측 기여도가 높아짐을 알수 있다.    

$$
\alpha_t = \frac{1}{2}\ln{\frac{1-\epsilon_t}{\epsilon_t}}
$$ (1)

<figure>
<figcaption>Figure.1</figcaption>
<img src="images/alpha_t.png" width=350px>
</figure>

## Update Data Weight
$$
e^{0.5\ln{\frac{1-e_t}{e_t}}}=\sqrt{\frac{1-e_t}{e_t}}
$$ (2)

$$
U_i^t = \begin{cases} 
\sqrt{\frac{e}{1-e}} \ \ \ if\  y_i = M_t(x_i), \ correct \ case \\\\\\
\sqrt{\frac{1-e}{e}}, \ \ \ if\ y_i \neq M_t(x_i) \ wrong \ case
 \end{cases}
\newline    
\newline    
$$ (2)
$$
D_i^{t+1}=\frac{D_i^{t}U_i^t}{\sum_{j=0}^{N}D_j^{t}U_j^t}
$$ (2)
<img src="images/update_w.png" width=350px>