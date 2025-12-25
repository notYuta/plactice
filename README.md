# plactice

シンプルな計算機モジュールとテストコードのプラクティスプロジェクト

## 概要

このプロジェクトには以下が含まれています：
- `calculator.py`: 基本的な算術演算を行う計算機モジュール
- `test_calculator.py`: pytestを使用した包括的なテストスイート

## セットアップ

```bash
# 依存関係のインストール
pip install -r requirements.txt
```

## テストの実行

```bash
# すべてのテストを実行
pytest

# 詳細な出力でテストを実行
pytest -v

# カバレッジレポート付きでテストを実行
pytest --cov=calculator --cov-report=html

# 特定のテストクラスを実行
pytest test_calculator.py::TestAddition -v
```

## 機能

### calculator.py

- `add(a, b)`: 2つの数を加算
- `subtract(a, b)`: 2つの数を減算
- `multiply(a, b)`: 2つの数を乗算
- `divide(a, b)`: 2つの数を除算（ゼロ除算チェック付き）
- `power(base, exponent)`: べき乗計算
- `is_even(number)`: 偶数判定
- `factorial(n)`: 階乗計算

### test_calculator.py

包括的なテストスイート：
- 各関数の基本的なテストケース
- エッジケースのテスト
- エラーハンドリングのテスト
- パラメータ化されたテスト
- 統合テストシナリオ

## テストカバレッジ

テストは以下をカバーしています：
- 正常系のテストケース
- 境界値テスト
- 例外処理のテスト
- 浮動小数点演算のテスト
- 負の数の処理