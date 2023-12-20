# 起動方法
最初にプロジェクト直下（docker-compose.ymlのあるフォルダ）で下記コマンドを実行してください。

```
docker-compose up -d
```
※ -dオプションはつけてもつけなくても問題ないです。

# フォルダ構成

```
プロジェクトフォルダ  
├── app   
│    ├── models：テーブルのモデルを格納しておくフォルダ  
│    │  
│    ├── static：デザイン（css）の実装フォルダ  
│    │  
│    └── templates：画面（html）の実装フォルダ  
│
└── .gitignore  
└── docker-compose.yml  
└── Dockerfile  
└── package-lock.json  
└── package.json  
└── requirements.txt  
└── tailwind.config.js  
```
