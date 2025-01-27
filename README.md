# README

```
PS> echo そのとき彼は「行けるならいくわ」と言うといった|scb
PS> uv run .\yure.py
PS> cat .\out\out.txt
イク	いく／行ける
ユウ	言う／いう
PS> cat .\out\out.txt|ConvertFrom-Csv -Delimiter "`t" -Header reading,variation

reading variation
------- ---------
イク    いく／行ける
ユウ    言う／いう

PS> cat in.txt
言う
云う
見る
観る
みる
取る
撮る
PS> uv run .\yure.py in.txt
PS> cat .\out\out.txt
ミル	見る／観る／みる
ユウ	言う／云う
```

---

[Sudachi](https://github.com/WorksApplications/Sudachi) and [SudachiDict](https://github.com/WorksApplications/SudachiDict) is licensed under the [Apache License, Version2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .
