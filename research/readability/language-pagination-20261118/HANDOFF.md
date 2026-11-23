# 公開研究交接：數學語言壓縮與自然分頁

## 1. 身份、授權與階段

- 交接ID：`CM-LANGUAGE-PAGINATION-PUBLICATION-20261118-v1`；公開文案v1；2026-11-18（Asia/Taipei）。精確提交時間與輸出commit以本檔所在Git提交為準，不在檔內虛構自己的commit。
- 發出：本輪研究負責人。接收：使用者及後續獲授權的研究／內容角色。對話公開URL未提供。
- 範圍：《Categorical Mathematics》V0–V2歷史案例及T1–T8、L1–L5隔離原型；本輪不是任何卷的新正式版次，未啟動A01–13或B-01–08。
- 狀態：研究完成後，使用者最新明確指示「整理結果git上去」，授權把研究整理到PR #1。原研究完成時「未修改GitHub」是當時狀態；本次後續授權新增公開研究提交，兩者分開記錄。
- 本次不修改正式／已發布／凍結正文、PDF、ReadFlow R1、A／B工作流、工具ZIP、分卷／文獻表或章號；不續改R7/P2/P3、不啟動其他卷。
- PR維持Draft；沒有合併main或採納新規則的授權。研究交付與出版採納、數學終審分開。
- 已核repository目前公開。此次發布僅原創研究文字、節錄、證據身份與診斷程式，不發布私人恢復入口、完整教材、原PDF、字型或第三方論文全文。

## 2. 固定基線、模型與A／B欄位

| 項目 | 固定身份／狀態 |
|---|---|
| 研究基線及本次提交父版本 | `4076cc01c41106be449ccd02e9c494a829bdd5f2` |
| 正式R1模板來源 | `8b9dc7f3749de81e47de9f525d7c5e0b3f8036c3` |
| R1正式採納紀錄 | `c749e4867538888d3069346fa055ac2ca834c9e1`，`archive/v0/readflow-r1-editorial-2026-11-17/TEMPLATE-ADOPTION.md` |
| 現行權威 | 來源導覽與版本映射v1 → A-B製作與交接總規範v4；固定來源入口與歷史限制v2 |
| 分卷／文獻表 | math-curriculum-v4-git-aligned.html／math-references-v4-git-aligned.html；身份見來源JSON，不是本輪全表新驗收 |
| 章號 | 沿固定交接V0 Ch0–9；V1 Ch10–28（前卷末9）；V2 Ch29–51（前卷末28）；本輪未重新逐章驗證整卷編號，未改號 |
| A／B | 本次為研究發布，不選用B；未明確選B的正式製作仍用A |
| 唯一正式正文 | 既有固定／凍結版本不變；研究B/S/F/C/I不是工作流B，也不是新正式正文 |
| B-05整卷整合輸入 | 不適用，未啟動；沒有章卷整合通過的新聲明 |
| 模型／模式 | 研究者及子代理實際後端路由、High設定、不同模型家族未核實；不聲稱已切換，不冒充正式四官 |

正式擴充／精修／排版GPT-6.1 Sol、粗規劃Terra、打厚依使用者指定的配置依v4保留。研究程序可嵌入原角色責任，沒有新逐章批准：擴充安排先備／敘事，打厚展開必要推理，精修核來源與安全壓縮，排版處理非語義行文與全頁視檢；排版後只由打厚最嚴格整卷終審，修正後回打厚複核。

## 3. 本次檔案manifest與可取入口

所有公開輸出的用途、版本、bytes與SHA256見[MANIFEST.json](./MANIFEST.json)；恢復本次固定版本使用其Git commit。manifest不含自己的自指hash，Git tree/blob固定其身份。上層README是可更新入口，不納入本目錄的固定成員檢查。

| 類別 | 入口 | 已核／未核邊界 |
|---|---|---|
| 結論 | [RESULTS.md](./RESULTS.md) | 原始觀察、外部研究、假說分列；非90分保證 |
| 歷史鑑識 | [FORENSICS.md](./FORENSICS.md)、[forensics.json](./evidence/forensics.json) | 九組頁面／文字定位與P2身份衝突；不附原圖 |
| 實驗 | [EXPERIMENTS.md](./EXPERIMENTS.md)、[experiment-record.json](./evidence/experiment-record.json) | 70+14頁結果、成功與失敗；非公開完整PDF重建包 |
| 數學義務／差異 | [semantic-cases.json](./evidence/semantic-cases.json)、[semantic-math-review.json](./evidence/semantic-math-review.json) | 八案的先備、義務、實際改句、反例與核對；不是全卷覆蓋表 |
| 原創例子 | [LANGUAGE-EXAMPLES.md](./LANGUAGE-EXAMPLES.md) | 自製判準例子，不冒充歷史稿件或外部實測 |
| 操作／問題單 | [ROLE-PROMPTS.md](./ROLE-PROMPTS.md)、[reading-defect.schema.json](./reading-defect.schema.json) | 七組完整草案；結構合格不代表內容正確 |
| 前綴審查 | [PREFIX-REVIEW.md](./PREFIX-REVIEW.md)、[prefix-adjudication.json](./evidence/prefix-adjudication.json) | 三項OPEN保留；非真人、非已核實跨模型 |
| 診斷工具 | [reading_diagnostics.py](./tools/reading_diagnostics.py)、[工具紀錄](./evidence/diagnostic-control.json)、tools/maps | 只定位候選；三已知正例／三對照不是盲測效能 |
| 來源／文獻 | [source-identities.json](./evidence/source-identities.json)、[literature.json](./evidence/literature.json) | 48固定輸入與10原始文獻／手冊紀錄；實讀範圍分列 |
| 模板／編譯依賴 | 固定R1 commit及原持有人研究包 | 不重發正式模板、字型或整包依賴；本目錄不能獨立編全部PDF |
| 公開核驗 | [verify.py](./verify.py) | 身份、語法、相對連結、私人定位資料；不評數學／閱讀 |

原持有人成果保持不動，私有恢復入口未公開：

| 檔案 | bytes | SHA256 |
|---|---:|---|
| Math_Language_Pagination_Research_v1.html | 5921526 | `8e20df9b1579387a3711f80d4e78b640e24247173fe95b649a70d8c20b68e59c` |
| Math_Language_Pagination_Research_Package_v1.zip | 82230783 | `ae2c7e9dc0b196c31b583c1f66b6d62f45c6949aa66fb610d3d9bfa15c8f8249` |
| 原始84頁PDF | 408262 | `34e8322d75094a2a723e0fe7bfaa028ee18cf2b93335783f617e035f4ee9460b` |
| 傳輸回讀84頁PDF | 433222 | `f3593b4964b0fadf44a3bd1f20a762a39a04d26e79868e38583322f2f0c64c44` |
| 完整內部交接TXT | 44028 | `bfaa815d8c4fb8917acf560fc4c8fdf5f3243a7b02be4f36e2f14182990699ce` |

兩個84頁PDF容器不同，但84頁逐頁文字、幾何、72dpiRGB及57書籤同；不合併為同一binary。公開版與持有人完整版用途不同，沒有宣稱所有原件都公開可取。

## 4. 來源PDF配對及實際核查

- 七個歷史ZIP CRC通過；P3完整來源manifest的2205檔身份通過。固定R7三ZIP還原隔離P2/P3；P3累積還原與完整包所有TeX相同，六個歷史marker／build-QA差異另列。
- 120個改動TeX在volume entry的literal input graph可達；這不是本輪全卷fresh編譯或新.fls證據。
- P2 841頁、P3 886頁機械統計；P3 CSV 886/886相同，P2 837/841相同，四筆差異不改164個超1750頁總數。P2舊hash位元未取回，評分當下精確檔案仍UNKNOWN。
- P3 ZIP與外置單檔886頁文字／幾何／72dpiRGB同，container hash不同；不能外推P2未取得版本。
- 歷史實際視檢九組、27頁次／25個不同物理頁；不是1727頁連續人工順讀。
- 語義五條件各14頁，共70頁；原型入口每案相同，clearpage只固定實驗邊界，會放大短尾。I只對T5限定長例題改樣式。
- 版面五組相同正文，10PDF共14頁；L2/L3 2→1，L1/L4/L5不變。L2同時改提示呈現與Needspace，L3同時改框、padding及行寬，非單一參數因果試驗。
- T5 I仍兩頁且失continued；L3/T5正文順序及先備不同，不能只歸因context高度。
- 57項數學義務局部AI核對；T2/T7共同修補後重核；精確有理數／SymPy另核有限矩陣與逆式。沒有正式證明檢查器或整卷終審。
- 實驗視檢：語義C1–14及I8–9共16頁實開；版面組10頁實開，其餘4頁與已看對照像素同。全70頁已渲染不等於逐頁已看。
- 前綴審查只讀10份context/C，不見B、作者理由；三先備／記號疑問OPEN。部分其他審查仍有研究背景暴露，不聲稱完全盲審。
- 定位工具三已知正例與三P2對照，missing anchor回UNKNOWN。Schema真實例與八種不合法記錄測試分列，不替代缺陷正確性。
- 持有人完整包在新目錄實際通過manifest、歷史還原及32正文／8context再生成，40TeX及cases.json完全相同；該搬移測試未fresh跑XeLaTeX。公開子集不含這些完整輸入。

原型原編譯以XeLaTeX每條件兩次，診斷無overfull／underfull／缺字／未定義引用／重複標記；歷史R1、P2/P3三卷未在本輪fresh重編。完整編譯順序為持有人包的prepare_inputs → create_semantic_experiments → build_semantic_experiments，另pagination_lab/build與combine_experiment_pdfs。Python／PyMuPDF、TeX Live套件、Noto Sans／DejaVu Sans Mono及包內字型版本留原log；未測跨平台位元重建。

## 5. 變更、角色與三層證據

本次只新增此研究目錄及更新上層README入口；原方法論、前輪研究、歷史經驗文件、正式書稿與模板都保留。沒有新全卷記號檔或覆蓋表；定義／證明／例子義務只對八樣本分列。研究T碼／L碼不是章號。

內容保留以數學義務與等價證據核；工程以來源、編譯、頁面與hash核；閱讀以指定視檢及問題定位核。真人偏好／理解／獨立應用／保留未測。三層互不替代。

特殊版面處理為R1隔離衍生層，沒有共用樣式升版。純視覺／非語義行文交排版；型別、量詞、先備、相等或證明疑問退精修，再按原責任轉擴充／打厚。最終仍只由打厚整卷終審及回修複核。

## 6. OPEN／UNKNOWN與責任

| ID／位置 | 影響／責任 | 阻塞範圍與下一步 |
|---|---|---|
| ID-P2-OLDPDF | 另組歷史hash未取得／來源協調 | 阻該版精確配對及評分位元認定，不阻限定比較；取得後再核 |
| ENG-HISTORICAL-FRESH | 三卷未fresh編譯／工程 | 阻新來源→PDF全卷認證；不以研究解凍 |
| S21-FONTS | 舊交接PDF身份／字型像素限制／工程 | 校準可用；阻未限定的精確工程金標 |
| PREFIX-T3-PI | 投影命名／精修 | 部署前查真實前文；常用慣例可能已足夠，不自動退稿 |
| PREFIX-T6-PREREQ | 連續性與pointwise先備／擴充、精修 | 部署前核已讀落點，不把未重教已知術語當證明錯誤 |
| PREFIX-T8-CONGRUENCE | 類相等與同餘銜接／精修 | 保留OPEN，不刪良定解釋 |
| LAYOUT-CONTINUATION | C5–6、T5 I、T6控制邊界／排版 | 阻整體套用patch；保留負結果，不再盲目加輪次 |
| TOOL-GENERALIZATION | 已知案例回歸／研究 | 阻跨卷可靠率主張；未見選段驗證 |
| HUMAN-OUTCOME | 新真人結果未測／研究、符合先備讀者 | 阻90分與學習效益宣稱；不新增每章使用者批准 |
| DOMAIN-SCALE | PDE等高階領域未實作／內容角色 | 阻162卷外推；按形態建立保留樣本 |
| PLATFORM-ACCESS | 瀏覽器互動／實機／可及性／跨平台未核／工程 | 靜態選段不代替相應認證 |
| MODEL-ROUTING | High／不同模型家族未核／協調 | 阻跨模型與完全盲審宣稱 |
| FORMAL-MATH | V0基礎、V1 FA01/FA02、V2第6步、16主題／22章映射及六全局門檻／原內容角色 | 沿原UNKNOWN與凍結；本研究不解除正式終審阻塞 |
| PUBLIC-INPUTS | 公開目錄不含原PDF／完整來源／研究持有人 | 阻宣稱公開全套可重現；身份與有限工具可核 |

## 7. 下一階段、驗收、傳遞與禁止重做

下一唯一階段：閱讀與評估這份研究提案；沒有自動啟動製作。若另獲試行授權，以未參與調整的代表選段驗證凍結判準；先處理已列先備與版面風險。

採用條件：數學義務無退步、保留樣本重現缺陷消除且無新增同級問題、題目頁例外與章卷銜接有效、閱讀與理解分列、可恢復可回退，再由使用者明確決定採納。正式稿仍須打厚唯一整卷終審。

停止條件：語義等價未核；密度達標卻拆散任務；跨場景失效且無適用條件；只有修改量／頁數／AI自評增加；來源與PDF身份矛盾。停止擴大不取消v4必要修正與打厚複核。

禁止：不重啟R7/P2/P3、不新開候選、不改正式模板／v4／工具ZIP／卷界／文獻表、不復活兩份NO OBJECTIONS、不因公開而合併main、不推倒已核研究重做。

待使用者決策：本次公開整理無待補資料／再批准事項。未來採用新方法是另一決策。傳遞：材料隨本次PR提交，完成回覆提供實際commit與遠端核驗；未私訊正式角色，未收到其讀入回執。公開可取≠已送指定角色≠實際讀入。

### 接收回執（實際接收者填）

- 交接ID／版本：
- 實際讀入檔案、版本／hash核對：
- 可讀／缺檔／權限失敗／版本衝突：
- 理解的角色、階段、A／B狀態、邊界、章號及凍結：
- 接受續作或僅受影響部分阻塞與理由：
- 下一唯一動作與不重做範圍：
