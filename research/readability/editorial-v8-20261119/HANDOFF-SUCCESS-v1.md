# v8 閱讀成功研究：完整交接

## 交接身份與狀態

- **交接 ID：**CM-V8-READING-SUCCESS-20261119-v1。
- **文案版本／日期：**v1，2026-11-19（Asia/Taipei）；研究整理於當地晚間完成。提交與遠端回讀的精確時間以 Git／PR 操作紀錄為準。
- **發出角色：**研究負責人；分工為量化重算、正文／PDF 案例核查、獨立成功歸因審查。這些是研究分工，不冒稱已切換成正式製作角色。
- **接收角色：**後續查閱研究的內容擴充、打厚、精修、行文排版與協調角色；本交接不啟動任何一位角色改書。
- **卷號／範圍：**V0–V2；連續 Chapters 0–51。V0 0–9，V1 10–28，V2 29–51；不重置章號、不改卷界。V0 是此範圍起卷，沒有本次須接續的前卷。
- **階段：**研究、只讀比較與研究發布完成；不是 A01–13／B-01–08 的正式教材製作階段。
- **A／B：**本次沒有另選 B，沒有變更任何卷的方案。方法參考映射 A04–12；僅已明確選 B 的卷才能使用相應 B 映射。
- **模型設定：**主研究模型依本次系統身份為 GPT-6 Astra Pro；研究分工沿用所提供的繼承設定。未由外部執行設定核驗具體推理檔位，記「未核實」，不冒稱切換 High 或已由指定正式角色模型完成終審。

## 本次授權與邊界

使用者先回報：「評分85-93之間的水準，每頁評分不太一樣。」「但整體已經能看，這個版本我算是滿意，書也已經提交github」。隨後明確要求：「研究成功原因並把成功git上」。

因此本次授權包含研究成功原因、讀取／比較已保存來源、整理研究成果及寫入既有 PR #1 的研究分支。**授權沒有擴張為改 v8 正文、重排凍結稿、修改正式模板、變更 A／B 或合併 main。** 本次交付只變更 `research/readability/` 之下的研究文件、證據與重核工具，並更新 PR 的研究說明。

使用者滿意是新的人類主觀閱讀證據，已明確記錄為成功。沒有把它冒稱每頁都有量測、平均 89、理解或延後保留通過，也沒有清除數學終審與歷史 OPEN。

## 有效基線與固定入口

| 層次 | 固定版本／路徑 | 實際處理 |
| --- | --- | --- |
| 來源導覽 | `來源導覽與版本映射-v1.txt`；SHA256 `099d845787542f49e0a2379e6fce0d9fbf78dc0fee58f7d9d901f262ebbd5a02` | 本次先全文讀取 |
| 現行規範 | `A-B製作與交接總規範-v4.txt`；SHA256 `bb095f08c70f79ecfb84abbabf3f1350ee7f53ba9de707c917a412301bac4fea` | 全文實讀；流程與唯一打厚終審不變 |
| 固定入口／歷史 | `固定來源入口與歷史限制-v2.txt`；SHA256 `26ace7d453b12b4f533dd2b478a9a6883ba4b030b7662cceeeb54dbee5ae8efa` | 全文實讀；不因歷史入口啟動工作 |
| 正式模板來源 | `8b9dc7f3749de81e47de9f525d7c5e0b3f8036c3` | ReadFlow R1 已採納；沒有新模板 |
| 模板採納紀錄 | `c749e4867538888d3069346fa055ac2ca834c9e1`，`archive/v0/readflow-r1-editorial-2026-11-17/TEMPLATE-ADOPTION.md` | 舊「未採納」措辭不能降格現行模板 |
| 成功書稿 | `60fe8d1910c06c309958edb9efcd20d63cbb08ac`，`archive/v0-v2/readflow-editorial-v8-2026-11-19/` | 只讀，來源與三份 reading PDF 重新下載、核 hash |
| 原始復盤 | `287d217676ab8119a29bdd83367c33545e5dff3d`，`research/readability/editorial-v8-20261119/` | 固定比較基線；原逐頁／逐章資料保留 |
| 前輪研究 | `85160acf73f40d1ff3eb5dafc184ee4c0cb5856e`，`research/readability/language-pagination-20261118/` | 延續既有安全壓縮與分頁方法，不重做隔離原型 |
| P3 歷史基線 | `4076cc01c41106be449ccd02e9c494a829bdd5f2` | 保留 70／68 回饋及硬密度門檻的負結果 |
| 輸出研究版本 | 本檔所在的新 Git 提交；PR #1 研究分支 | 不是書稿 commit；提交完成後在交付訊息提供完整 commit 與遠端核對結果 |

分卷表、文獻表、正式覆蓋表與教材邊界本次未變更，也未重新驗收。未查的全局覆蓋與 v4 歷史未知不能因本次研究清零。

## 輸入檔案身份與來源／PDF 配對

完整 bytes、SHA256、用途、可取位置與本次核驗結果在 [success-verification.json](evidence/success-verification.json)。主要身份如下：

| 檔案 | bytes | SHA256 |
| --- | ---: | --- |
| v8 Source.zip | 4,207,686 | `6226f04971e5a097bd25ba685293840dc99aefed71ca7cf8d175b0f8694c81fe` |
| v8 reading/volume-0.pdf | 1,906,293 | `4d931401a3bcbec3d7bae6b593c8e7d98d2821ac76c577ea40441f9631f15e85` |
| v8 reading/volume-1.pdf | 676,184 | `4bc998ed7a28d073247fe863036f875c4af3dec3c391e5e9349da452bd19eb43` |
| v8 reading/volume-2.pdf | 900,904 | `ad29b6392b95938ff9f471c05a6f53332f4afda1761d4c43818a6166dbb59537` |
| P2 scoring/volume-0.pdf | 1,917,650 | `ac173bc6a2bd1812ab9cf2100597950bf0e524236d3384f6525049dfd8260fa3` |
| P2 scoring/volume-1.pdf | 669,561 | `60a44b7df6dbed93367269f8cc5092d7670cea109fad506580bc4c88ecfb596c` |
| P2 scoring/volume-2.pdf | 885,901 | `e9142336256daca9b347e2df7fa2cf4b0f7432e9693ef350ab93e9714ea171f1` |

v8 可取入口為上表固定書稿 commit 的公開 archive。原始來源 ZIP 及三份 reading PDF 全部重新實算 bytes/hash，ZIP CRC 通過；包內 manifest 的 309 檔全部核對，三份包內 PDF 與公開 PDF 逐位元相同。

P2／P3 原始研究包已恢復並核 SHA256 `ae2c7e9dc0b196c31b583c1f66b6d62f45c6949aa66fb610d3d9bfa15c8f8249`（82,230,783 bytes，617 ZIP members）；來源差分只在隔離副本套用，使用原腳本逐項核基線和前後 hash。私人恢復入口、完整歷史 PDF／ZIP、第三方全文與字型沒有重新公開。公開研究可重算 CSV 統計；若未持有歷史原檔，不能宣稱可由本目錄獨立重建所有 P2／P3 頁面。

來源包所載重建方式為 `python verify.py`、`python build-edition.py --entry volume` 或 `--entry print`；依賴 Python 3、XeLaTeX、原 R1 套件與指定字型，順序 V0→V1→V2 更新跨卷索引。本次只執行身份核驗 `verify.py`，**未執行教材編譯**，未下載核驗六份中的三份 print PDF。不要把此交接讀成 fresh build 回執。

## 研究產出清單

每檔版本、用途、bytes、SHA256 與相對可取路徑列在 [SUCCESS-MANIFEST.json](SUCCESS-MANIFEST.json)。manifest 不自引自身 hash；其身份由承載它的 Git commit 固定。

| 產出 | 用途 |
| --- | --- |
| [SUCCESS-ANALYSIS.md](SUCCESS-ANALYSIS.md)／[HTML](SUCCESS-ANALYSIS.html) | 完整成功原因、實例、數據、反例、因果限制與推薦 |
| [REUSE-GUIDE.md](REUSE-GUIDE.md) | 既有角色可用的操作與 Prompt 草案、KEEP／退回／停止規則 |
| [success-feedback.json](evidence/success-feedback.json) | 使用者直接回饋、發布授權與未測欄位 |
| [success-cases.json](evidence/success-cases.json)／[diffs](evidence/diffs/) | 4 組前後來源、24 項局部義務、PDF 頁碼與實際差異 |
| [success-exercise-cases.json](evidence/success-exercise-cases.json) | P3 題目／短解分離在 v8 的實際對照 |
| [success-metrics.json](evidence/success-metrics.json) | 獨立重算 52 章與 1,663 頁，含口徑及次序依賴分解 |
| [success-pdf-counts.json](evidence/success-pdf-counts.json) | PDF 重抽字元，保留固定裁切失敗與正確排除頁眉頁腳的重核 |
| [success-source-controls.json](evidence/success-source-controls.json) | 294 個可達輸入與局部分頁控制 |
| [success-boundary-observations.json](evidence/success-boundary-observations.json) | 兩個頁尾重疊 OPEN 的文字座標與來源對應 |
| [success-verification.json](evidence/success-verification.json) | 輸入身份、三層檢查範圍、未做事項 |
| [recompute-success-metrics.py](tools/recompute-success-metrics.py) | 按固定來源重算描述統計，不產可讀性分數 |
| [verify-success-pdfs.py](tools/verify-success-pdfs.py) | 以持有的固定 P2／v8 PDF 核身份及1,663頁字元；不改PDF |
| [verify-success.py](tools/verify-success.py) | 核公開產出 hash、JSON、必要檔案及連結；非數學／閱讀驗收 |
| 本交接 | v4 所需階段、來源、範圍、責任、OPEN 與下一步 |

研究根 README 與 v8 原復盤新增後續回饋入口；原資料不被新回饋覆寫成「當時早已知道」。舊研究的實驗結果與失敗紀錄保留。

## 完成範圍與三層證據

**內容層：**四組改前／改後來源實讀，24 項局部數學義務核查；另核兩組習題的有限計算與必要條件。沒有整卷定理重證、全表文獻覆蓋或打厚終審。

**工程層：**v8 源包／reading PDF hash、CRC、309 檔 manifest、包內外 PDF 配對；P2／P3 隔離還原；1,663 頁 PDF 有效字元與 CSV 全部相符；52 章數據核對；294 個 literal input 可達檔、0 個未解析 literal input。正式教材未重編，不能以輸入身份一致替代編譯與語義。

**閱讀層：**使用者直接滿意回饋已記錄；研究實際比較 20 個不同完整頁面影像，另檢 2 個頁尾局部；沒有 886 頁連續人工順讀。PDF 視檢列頁清單、未檢範圍和局部反例，未由 AI 自評產生分數。

**公開文件層：**產出 manifest、JSON／Python 語法、研究連結、公開範圍與 HTML 檢查；Git 推送後逐檔讀回核內容與 blob。遠端完成的證據以最終交付回覆及 Git 為準，不預填未發生的推送成功。HTML 的靜態連結／內嵌圖片已核；Chromium 在載入頁面前遭環境拒絕 socket，改作離線列印預覽，未聲稱完成瀏覽器桌面／手機實看。

## OPEN／UNKNOWN 與責任

| ID | 位置／影響 | 責任角色 | 是否阻研究發布／下一步 |
| --- | --- | --- | --- |
| OPEN-V8-FOOTER-01 | V0 PDF 274／印262，正文與左頁腳及頁碼區重疊 | 行文排版；若將來獲授權修，修後回打厚依原流程複核 | 不阻研究；本輪只登錄，不改書 |
| OPEN-V8-FOOTER-02 | V2 PDF 175／印166，正文末行與左頁腳重疊 | 行文排版；同上 | 不阻研究；不可因滿意回饋清零 |
| TRADEOFF-39-5 | P2 題解同頁，v8 題目113／解答114；解答本身完整 | 排版／內容依實際缺陷判斷 | 不是自動失敗或改稿命令；保留局部取捨 |
| UNKNOWN-V4-INTERMEDIATE | 未取回本輪編輯中間稿；無法獨立重現原復盤的等號後斷頁、收尾修補、Ch1 對 v4 全相同 | 研究來源管理 | 不阻固定成品比較；只引作者紀錄，不假稱實核 |
| UNKNOWN-P2-OTHER-BYTES | 舊交接另組 PDF hash 仍未取回；精確評分時位元同一性未獨立觀察 | 版本管理／研究 | 不阻已固定 scoring PDF 比較；不得把兩組混稱相同 |
| UNKNOWN-SCORE-MAP | 沒有逐頁分數、受測頁清單、裝置、平均值 | 研究測量 | 不阻記錄滿意；不得製造量表或平均 |
| UNKNOWN-CAUSAL | 改法、熟悉度、次序、裝置與選段未控制 | 研究設計 | 不阻方法假說；不能分配每項貢獻分數 |
| UNKNOWN-AUTONOMY | 完整人類逐章介入量未知；162 卷／跨域自主重現未測 | 後續已授權製作角色與研究 | 不阻保存成功；未來按實際介入與回歸證據檢驗 |
| OPEN-MATH-INHERITED | v8 獨立整卷數學終審、先備／文獻覆蓋未決；V2 Stage6 精修仍待 | 精修／打厚，依原階段 | 不阻研究；仍限制正式數學通過主張 |
| UNKNOWN-GLOBAL-INHERITED | v4 記錄的全局未知及規劃對照未由本研究處理 | 原責任角色 | 不清零、不啟動其他卷 |
| NOT-RUN-BUILD | 沒有本次 fresh XeLaTeX 重編或 print PDF 重核 | 工程／排版 | 不阻來源分析；不能稱本次重編通過 |

兩個頁尾項相關位置有正向擴頁命令，但未做移除後重編，不宣稱唯一原因。規範中的特殊排版、風險及修補責任欄位在此保留；本輪沒有新增模板 patch、沒有共用樣式升版、沒有正文依賴變更。

## 下一步、通過條件與禁止重做

**本次唯一下一步：**完成研究分支提交並核遠端，交付使用者研究入口及 commit；之後保留滿意的 v8。這不指派下一卷或新的教材修訂。

後續角色只有在另有已授權工作時，才按本草案重用案例。接受條件為：實讀固定來源、核數學義務、指出具體阻力消失、檢查相鄰頁與受影響依賴；正式最終仍由打厚唯一整卷終審。沒有逐章等待使用者批准。

禁止事項：不覆寫 v8 或凍結稿；不重做已核成功章；不為每頁追 93 分啟動大量改稿；不把 1,750 字元重新立為通過門檻；不改 R1、A／B、分卷／文獻表、工具 ZIP 或章號；不清零歷史 OPEN；不因研究自行合併 PR 或啟用 B。

待使用者決策：**無阻塞性待決。** 研究發布已明確授權；不需要再次請求批准。研究結果不自動構成新方法正式採納。

## 傳遞狀態與接收回執

本文是完整可取的交接文案，隨研究 commit 發布於 PR #1。Git 遠端核對只證明已提交可取，不代表各正式角色已讀入或接受。未對其他人送訊，未收到正式角色接收回執；如果將來需要在其他對話使用，可轉貼本交接固定 Git 連結。

接收方回執應列：交接 ID／版本、實際讀入檔與 hash、可取或缺檔、理解的授權／A或B／角色／章號／凍結範圍、接受或僅受影響部分阻塞、下一步與不重做項。不能只以「已看過研究」當作已讀固定正文。
