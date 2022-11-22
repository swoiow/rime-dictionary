## Rime 扩展词库


## 最佳实践

## 自用级 `pinyin_plus.dict.yaml`

```yaml
name: pinyin_plus
version: "2022.11.22"
sort: by_weight
use_preset_vocabulary: true
import_tables:
  # pinyin_plus, 放于第一行，用作用户自造词。需要与`name`保持一致。
  - pinyin_plus
  - luna_pinyin
  - extended\userdict
  - extended\xhzd
  - extended\tsinghua.ocl
  - extended\qqpy.default
  - extended\qqpy.usually
  - extended\sougou.chengyu
  - extended\sougou.netword
```

## 说明

根据RIEM的介绍，文件名和`dict.yaml`里面的`name`字段应该为一致的。

- [关于码表的格式](https://github.com/rime/home/wiki/DictionaryPack#%E7%A4%BA%E4%BE%8B)
- [導出及導入文本碼表](https://github.com/rime/home/wiki/UserGuide#%E5%B0%8E%E5%87%BA%E5%8F%8A%E5%B0%8E%E5%85%A5%E6%96%87%E6%9C%AC%E7%A2%BC%E8%A1%A8)
  - 以製表符（Tab）分隔的三列，分別是文字、編碼、使用頻次。其中，編碼是碼表中定義的完全形式，多個音節間以空格。
  - `<輸入法語言代號>.userdb/` - 輸入法程序爲保存用戶的輸入習慣而創建的 用戶詞典。
- [碼表與詞典](https://github.com/rime/home/wiki/RimeWithSchemata#%E7%A2%BC%E8%A1%A8%E8%88%87%E8%A9%9E%E5%85%B8)
  - 使用頻次，往往用于多音字的场景

---

1. 除了《新华字典》，《现代汉语词典》外，其他词库均去除单字词条。
2. `use_preset_vocabulary`，是否導入預設詞彙表【八股文】。扩展词库默认设置为`false`。

+ `xhzd.dict.yaml`
  - 新华字典，有词频，[来源](https://github.com/swoiow/rime-dictionary/tree/main)

+ `qqpy.default.dict.yaml`
  - QQ拼音默认词库，无词频，[来源](http://cdict.qq.pinyin.cn/v1/)

+ `qqpy.usually.dict.yaml`
  - 常用聊天短语，无词频，[来源](http://cdict.qq.pinyin.cn/v1/)

+ `sogou.default.dict.yaml`
  - 搜狗拼音默认词库，无词频，[来源](https://pinyin.sogou.com/dict/)，其他细节见补充

+ `sougou.chengyu.dict.yaml`
  - 搜狗拼音默认词库，无词频，[来源](https://pinyin.sogou.com/dict/)，其他细节见补充

+ `sougou.netword.dict.yaml`
  - 搜狗拼音网络新词，无词频，[来源](https://pinyin.sogou.com/dict/)，其他细节见补充

+ `tsinghua.ocl.dict.yaml`
  - 清华大学开放中文词库，无词频，[来源](https://github.com/redguardtoo/pyim-tsinghua-dict)，见[项目](https://github.com/thunlp/THUOCL)


## 补充

转换，工具，及其他见[分支](https://github.com/swoiow/rime-dictionary/tree/main)
