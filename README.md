<html lang="ja">
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1><center>Slider</center></h1>
        <h2>なにものか？</h2>
        <p>
            Matplotlib の Slider を使って色々なパラメータを動かしてグラフの変化を眺めるプログラムです。<br>
            <br>
            ・PWM (Pulse Width Moduration）<br>
            <img src="images/PWM.gif"><br>
            　　duty比: 入力パルスの High期間とLow期間の比率<br>
            　　tau：   時定数。充電の速度<br>
            <br>
            ・ROC (Receiver Operating Characteristic)<br>
            <img src="images/ROC.gif"><br>
            <br>
            ・ベータ分布<br>
            　alpha－1.0：表の出た回数、beta－1.0：裏の出た回数の事後確率分布に対応している。<br>
            <img src="images/beta.gif"><br>
            <br>
            ・ベルヌーイ分布<br>
            　横軸 0.0、1.0 がコイントスの裏の出る事象、表のでる事象。<br>
            　lambdaが表の出る確率に対応している。<br>
            <img src="images/Bernoulli.gif"><br>
            <br>
            ・正規分布<br>
            <img src="images/normal.gif"><br>
        </p>
        <h2>環境構築方法</h2>
        <p>
            pip install opencv-python scipy matplotlib
        </p>
        <h2>使い方</h2>
        <p>
            ・PWM<br>
            　python src\Slider_PWM.py<br>
            <br>
            ・ROC<br>
            　python src\Slider_ROC.py<br>
            <br>
            ・ベータ分布<br>
            　python src\Slider_Beta_Distribution.py<br>
            <br>
            ・ベルヌーイ分布<br>
            　python src\Slider_Bernoulli_Distribution.py<br>
            <br>
            ・正規分布<br>
            　python src\Slider_Normal_Distribution.py<br>
            <br>
        </p>
    </body>
</html>
