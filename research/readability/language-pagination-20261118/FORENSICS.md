# P2／P3 頁面與來源鑑識

> **公開整理 v1｜2026-11-18。** 本研究原先只做比較與隔離試驗；研究完成後，使用者另明確授權把結果提交 PR #1。本次只發布研究文字、結構化紀錄與診斷工具。正式 ReadFlow R1 已採納；以下新提案未採納，A／B 工作流與正式／凍結稿不變。
>
> 沒有新人類閱讀／理解／應用／保留測試，沒有「已穩定90分」的結論。本公開目錄不附私人原始PDF、完整教材、字型或恢復入口，不能單靠本目錄重建全部歷史頁面。固定比較基線仍為 `4076cc01c41106be449ccd02e9c494a829bdd5f2`。


完整身份、機械統計及P2版本衝突見 [forensics.json](./evidence/forensics.json)。以下沿原案例ID列定位，不聲稱每個補丁均已做單獨消融。

## F01 · new continuity defect

**volume**

V2

**source**

editorial_r7/014-prime-factorization.tex

**P3_lines**

64–72

**control**

L67: \enlargethispage{-8\baselineskip}

**quote_before**

The bounded-search theorem therefore gives a whole-source least index, not just local existential witnesses. Let $p(r)$ be that index plus two.

**quote_after**

Same mathematical prose; PDF 134 ends before “Let p(r) be that index plus two”, which begins PDF 135.

**observation**

原本同段的選中索引與 p(r) 命名，被翻頁分開。下一頁首行依賴 that index；後續公式又依賴 p(r)。

**interpretation**

回指距離增加；縮頁讓頁底留白，沒有沿段落邊界斷開。控制命令與PDF位置支持此機制，但未逐一關閉命令做消融。

**severity**

reader-context risk

**source_sha256**

```json
{
  "P2": "e1fa64cb3bfeb0e1eb434e9fb5fa8d2eb0cb4e24fa3790b06ac3275635e16bb7",
  "P3": "d89dda86996c7a150a6ed2b0c67b0021845f9dca26d9ff6397a692b9277e16cb"
}
```

**page_records**

```json
[
  {
    "volume": "V2",
    "version": "P2",
    "physical_page": "129",
    "chars": "1664",
    "extended_chars": "1664",
    "body_y0": "65.08",
    "body_y1": "651.94",
    "occupied_y_span": "586.86",
    "footer": "V2 / ReadFlow R1 / R7-P2 scoring draft | 120",
    "start": "on each stable source part. Moreover 𝑣𝑝(1) = f: an equation 1 = 𝑝𝑤with 𝑝≥2 is impos- sible on a noninitial par",
    "end": "ion on the counter 𝑖 constructs a state with four natural coordinates (𝑟0, 𝐶0, 𝑃0, 𝑈0) = (𝑛, 0, 1, 1), (𝑟, 𝐶, 𝑃, 𝑈) ⟼􏿴𝑣(𝑟), 𝐶+ 𝑝(𝑟)𝑈, 𝑃𝑝(𝑟), 𝐵𝑈􏿷. (F1)"
  },
  {
    "volume": "V2",
    "version": "P3",
    "physical_page": "134",
    "chars": "1557",
    "extended_chars": "1557",
    "body_y0": "68.56",
    "body_y1": "545.05",
    "occupied_y_span": "476.49",
    "footer": "V2 / ReadFlow R1 / R7-P3 scoring draft | 123",
    "start": "pf. Let 𝑔= 𝐺(𝑝, 𝑎). The gcd construction supplies 𝑔∣𝑝. On each represented factor- ization 𝑝= 𝑔𝑐, primality fo",
    "end": "ange and tests true, since it is 𝑟itself. The bounded-search theorem therefore gives a whole-source least index, not just local existential witnesses."
  },
  {
    "volume": "V2",
    "version": "P3",
    "physical_page": "135",
    "chars": "1190",
    "extended_chars": "1190",
    "body_y0": "68.64",
    "body_y1": "554.19",
    "occupied_y_span": "485.55",
    "footer": "V2 / ReadFlow R1 / R7-P3 scoring draft | 124",
    "start": "Let 𝑝(𝑟) be that index plus two. The preceding proposition proves that it is prime, and division supplies 𝑣(𝑟)",
    "end": "otal arrow 𝑎∶𝑁× 𝑃+ →𝑁; no extension of an arbitrary map on 𝐼𝑖has been assumed. The equalizer for 𝑛= 𝑃𝑖𝑟𝑖is invariant because (𝑃𝑖𝑝(𝑟𝑖))𝑣(𝑟𝑖) = 𝑃𝑖𝑟𝑖= 𝑛."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F02 · new isolated solution tail

**volume**

V1

**source**

editorial_r6/sections/64-direct-images.tex

**P3_lines**

200–214

**control**

L207: \enlargethispage{-5\baselineskip}

**quote_before**

The image $f_*m$ is the whole singleton, and its pullback along $b$ is again the whole singleton. But $a^*m$ has empty domain and target $X'$, so its image under $f'$ is the empty subset of $Y'$.

**quote_after**

Same full solution moved to a new chapter-end PDF page 104.

**observation**

Exercise 23.7 題目留在 P3 103，解答在104，後者標準裁切312字元、文字縱向跨度77.68pt。P2題目與解答同在99。

**interpretation**

低於密度上限並未避免孤立末頁；300字元短頁警示會漏掉這個312字元例子。題目與詳解可分頁，但本例新增一整張只承載短解答，應整組比較閱讀成本。

**severity**

pagination regression

**source_sha256**

```json
{
  "P2": "3590508f10c4c4ecc016018bff9c9de2b23af82e884019c4ee8935d200350936",
  "P3": "4c580faefc84636575a37878133c75f2e06ae5178a30646eda492cade46a6045"
}
```

**page_records**

```json
[
  {
    "volume": "V1",
    "version": "P2",
    "physical_page": "99",
    "chars": "1893",
    "extended_chars": "1893",
    "body_y0": "68.56",
    "body_y1": "680.32",
    "occupied_y_span": "611.76",
    "footer": "V1 / ReadFlow R1 / R7-P2 scoring draft | 91",
    "start": "pf. Take the pullback 𝑇of 𝑓𝑚∶𝑀→𝑌and 𝑛∶𝑁→𝑌, with 𝑢∶𝑇→𝑀, 𝑣∶𝑇→𝑁. The arrow 𝑚𝑢∶𝑇→𝑋is monic: 𝑢is the pullback of th",
    "end": " the compatible identity maps from a singleton to 𝑋, 𝑌′ would require a map into the empty 𝑋′. Thus the extra point in the true pullback is essential."
  },
  {
    "volume": "V1",
    "version": "P3",
    "physical_page": "103",
    "chars": "1581",
    "extended_chars": "1581",
    "body_y0": "68.56",
    "body_y1": "582.37",
    "occupied_y_span": "513.81",
    "footer": "V1 / ReadFlow R1 / R7-P3 scoring draft | 94",
    "start": "pf. Take the pullback 𝑇of 𝑓𝑚∶𝑀→𝑌and 𝑛∶𝑁→𝑌, with 𝑢∶𝑇→𝑀, 𝑣∶𝑇→𝑁. The arrow 𝑚𝑢∶𝑇→𝑋is monic: 𝑢is the pullback of th",
    "end": " 𝑏= id, and 𝑋′ empty with its unique maps 𝑎, 𝑓′. With 𝑚= id𝑋, compute both sides of the change-of-base equation and explain the missing pullback test."
  },
  {
    "volume": "V1",
    "version": "P3",
    "physical_page": "104",
    "chars": "312",
    "extended_chars": "312",
    "body_y0": "65.08",
    "body_y1": "142.76",
    "occupied_y_span": "77.68",
    "footer": "V1 / ReadFlow R1 / R7-P3 scoring draft | 95",
    "start": "Solution. The image 𝑓∗𝑚is the whole singleton, and its pullback along 𝑏is again the whole singleton. But 𝑎∗𝑚ha",
    "end": " the compatible identity maps from a singleton to 𝑋, 𝑌′ would require a map into the empty 𝑋′. Thus the extra point in the true pullback is essential."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F03 · new isolated solution tail

**volume**

V1

**source**

editorial_r6/sections/69-descent-and-saturated-conditions.tex

**P3_lines**

161–214

**control**

L161 -5, L181 -7, L194 -4, L202 -5 baselineskip

**quote_before**

Precomposing with $q$ gives $(s\bar h)q=l=(t\bar h)q$, hence $s\bar h=\bar l=t\bar h$ by epicity of $q$.

**quote_after**

Same Exercise 25.8 solution starts an otherwise almost empty new page 129.

**observation**

P2 121同頁題解，P3 128題／129解。129含351有效字元、文字縱向跨度77.77pt。

**interpretation**

多個沿舊頁碼加入的負向頁高控制串聯，密度達標卻把一個短核對單位拆成兩頁。這不是缺少數學文字，而是分頁預算位置不當。

**severity**

pagination regression

**source_sha256**

```json
{
  "P2": "5534fb8bf7c15e745706dabbbf435e146d4adb3e72ea8ee169563724332c995e",
  "P3": "364d1aba1e4eb8fe13fb63397575f156993273ce0a19e0d8631782a41db6a871"
}
```

**page_records**

```json
[
  {
    "volume": "V1",
    "version": "P2",
    "physical_page": "121",
    "chars": "1801",
    "extended_chars": "1801",
    "body_y0": "68.64",
    "body_y1": "590.02",
    "occupied_y_span": "521.39",
    "footer": "V1 / ReadFlow R1 / R7-P2 scoring draft | 113",
    "start": "The invariant function with block values 𝑥, 𝑦descends uniquely to the function send- ing 0 to 𝑥and 1 to 𝑦; the",
    "end": "ant 0, 𝑡= id𝑋, and 𝑙selecting 0. Then 𝑠ℎ= 𝑙= 𝑡ℎand 𝑠≠𝑡. Descent reflects equations on its target 𝐵, not arbitrary equality beyond the displayed image."
  },
  {
    "volume": "V1",
    "version": "P3",
    "physical_page": "128",
    "chars": "1294",
    "extended_chars": "1294",
    "body_y0": "69.89",
    "body_y1": "432.61",
    "occupied_y_span": "362.72",
    "footer": "V1 / ReadFlow R1 / R7-P3 scoring draft | 119",
    "start": "Exercise 25.7 (Why the kernel pair matters). Use the noneffective relation on the fully marked 𝐴= {0, 1} from ",
    "end": "et invariant ℎ∶𝐴→𝑋 and 𝑙∶𝐴→𝑌have descended maps ̄ℎ, ̄𝑙. For two arrows 𝑠, 𝑡∶𝑋→𝑌satisfying 𝑠ℎ= 𝑙= 𝑡ℎ, what equality is forced on 𝐵? Does it force 𝑠= 𝑡?"
  },
  {
    "volume": "V1",
    "version": "P3",
    "physical_page": "129",
    "chars": "351",
    "extended_chars": "351",
    "body_y0": "65.08",
    "body_y1": "142.85",
    "occupied_y_span": "77.77",
    "footer": "V1 / ReadFlow R1 / R7-P3 scoring draft | 120",
    "start": "Solution. Precomposing with 𝑞gives (𝑠̄ℎ)𝑞= 𝑙= (𝑡̄ℎ)𝑞, hence 𝑠̄ℎ= ̄𝑙= 𝑡̄ℎby epicity of 𝑞. This does not force 𝑠",
    "end": "ant 0, 𝑡= id𝑋, and 𝑙selecting 0. Then 𝑠ℎ= 𝑙= 𝑡ℎand 𝑠≠𝑡. Descent reflects equations on its target 𝐵, not arbitrary equality beyond the displayed image."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F04 · exercise statement split on mixed page

**volume**

V0

**source**

editorial_r3/views/v0/sections/01-opening.tex

**P3_lines**

255; 296–309

**control**

L255: \enlargethispage{-5\baselineskip}, earlier on the chapter flow

**quote_before**

Use the same row/column convention as Example~\ref{ex:idempotent}. Check that $e$ satisfies the identity laws, then use a triple to show that this is not a category.

**quote_after**

The table is on PDF 50; the instruction is in an Exercise 1.3 (continued) box at the top of PDF 51.

**observation**

P2 44 的 Exercise1.3 表格與作答指令同頁；P3 50/51分開。50是正文結尾與習題混合頁，不宜套全頁一個密度門檻。

**interpretation**

表格＋條件＋動作指令是一個可保護的短題目單位；P3新增跨頁會迫使回看表格。此例直接支持習題題目與一般敘事分流。

**severity**

exercise-unit regression

**source_sha256**

```json
{
  "P2": "9b4b9dd16e3d73f894f96241de48fe51d063fd4f0bfd3efbaf2031e705f543e2",
  "P3": "6bf2580a8b6f35b8c855d969a5ee7b31d82961a84cebd84b40a0f3379d22c070"
}
```

**page_records**

```json
[
  {
    "volume": "V0",
    "version": "P2",
    "physical_page": "44",
    "chars": "1315",
    "extended_chars": "1315",
    "body_y0": "68.64",
    "body_y1": "602.3",
    "occupied_y_span": "533.66",
    "footer": "V0 / ReadFlow R1 / R7-P2 scoring draft | 32",
    "start": "or a later internal number object. A nonunique family of construction choices must itself be supplied, or its ",
    "end": " 𝑒 Use the same row/column convention as Example 1.13. Check that 𝑒satisfies the identity laws, then use a triple to show that this is not a category."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "50",
    "chars": "1561",
    "extended_chars": "1561",
    "body_y0": "68.64",
    "body_y1": "650.24",
    "occupied_y_span": "581.6",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 35",
    "start": "automatically existing object. Object and arrow ranges need not be sets; this wording does not assert that arb",
    "end": "estion. Exercise 1.3 (Associativity still has to be checked). On one object 𝑃, take ar- rows 𝑒, 𝑎, 𝑏∶𝑃→𝑃with the table ∘ 𝑒 𝑎 𝑏 𝑒 𝑒 𝑎 𝑏 𝑎 𝑎 𝑏 𝑒 𝑏 𝑏 𝑒 𝑒"
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "51",
    "chars": "1404",
    "extended_chars": "1404",
    "body_y0": "65.2",
    "body_y1": "671.56",
    "occupied_y_span": "606.36",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 36",
    "start": "Exercise 1.3 (continued) Use the same row/column convention as Example 1.13. Check that 𝑒satisfies the identit",
    "end": "on with- out values. The next chapter asks when a route can be reversed: returning to its source must recover the identity, at both ends of the arrow."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F05 · new short chapter-end continuation

**volume**

V0

**source**

editorial_r7/005-b01-subcategories-and-groupoids.tex

**P3_lines**

170–180

**control**

L170: \enlargethispage{-5\baselineskip}

**quote_before**

For the all-identities selection, a composable pair $\id_X,\id_Y$ requires $X=Y$ and composes to that same identity.

**quote_after**

Same final part of Exercise 2.3 solution moved to PDF 71.

**observation**

P3 71僅313字元、74.12pt文字跨度；P2 64可容納整段。P2原頁視覺偏滿，P3前頁確有減負，但成本是另開一頁。

**interpretation**

保留密度改善的局部事實，同時判定全閱讀單位被拆散。不能把每個減密頁都視為收益。

**severity**

pagination tradeoff requiring redesign

**source_sha256**

```json
{
  "P2": "72dc2cb033b9122844c82ef9b9afac8e120a7e973eba4123da465aa9b3393637",
  "P3": "6a0080b7cdcfa915ec1aa4c9bbe404b27b7846266ac217e5c3eb759e5c8b8052"
}
```

**page_records**

```json
[
  {
    "volume": "V0",
    "version": "P2",
    "physical_page": "64",
    "chars": "1860",
    "extended_chars": "1860",
    "body_y0": "63.1",
    "body_y1": "679.9",
    "occupied_y_span": "616.81",
    "footer": "V0 / ReadFlow R1 / R7-P2 scoring draft | 52",
    "start": "2.7 Practice: closure is part of the data Exercise 2.2 (Two possible reversible parts). For the four functions",
    "end": "row in 𝒞is an identity, which is the discrete-category condition: fullness now tests every original pair of objects because all objects were retained."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "70",
    "chars": "1547",
    "extended_chars": "1547",
    "body_y0": "63.1",
    "body_y1": "600.2",
    "occupied_y_span": "537.11",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 55",
    "start": "2.7 Practice: closure is part of the data Exercise 2.2 (Two possible reversible parts). For the four functions",
    "end": "her such arrow. These are all arrows of 𝒞with endpoints in the one-object selection, which proves fullness. The inherited laws prove it is a category."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "71",
    "chars": "313",
    "extended_chars": "313",
    "body_y0": "68.64",
    "body_y1": "142.76",
    "occupied_y_span": "74.12",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 56",
    "start": "For the all-identities selection, a composable pair id𝑋, id𝑌requires 𝑋= 𝑌and com- poses to that same identity.",
    "end": "row in 𝒞is an identity, which is the discrete-category condition: fullness now tests every original pair of objects because all objects were retained."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F06 · mixed improvement and regression

**volume**

V2

**source**

editorial_r7/014-prime-factorization.tex

**P3_lines**

45–56

**control**

L49: \enlargethispage{-5\baselineskip}

**quote_before**

$v_p(xy)=v_p(x)\lor_2 v_p(y)$ on each stable source part.

**quote_after**

Same display and its source qualification now occur together on P3 PDF 134.

**observation**

P2 128底端公式與129首行 on each stable source part 分離；P3 134把整個證明放一起。但命題42.5留在133，證明在134，且134→135另產生F01。

**interpretation**

同次改動可以修復一個相鄰關係並破壞另一個；應審查命題／證明／下一段整個窗口。不能把P3全部頁面一律判壞，也不能用單一改善頁證明整體成功。

**severity**

mixed outcome

**source_sha256**

```json
{
  "P2": "e1fa64cb3bfeb0e1eb434e9fb5fa8d2eb0cb4e24fa3790b06ac3275635e16bb7",
  "P3": "d89dda86996c7a150a6ed2b0c67b0021845f9dca26d9ff6397a692b9277e16cb"
}
```

**page_records**

```json
[
  {
    "volume": "V2",
    "version": "P2",
    "physical_page": "128",
    "chars": "1879",
    "extended_chars": "1879",
    "body_y0": "72.87",
    "body_y1": "680.74",
    "occupied_y_span": "607.86",
    "footer": "V2 / ReadFlow R1 / R7-P2 scoring draft | 119",
    "start": "Proposition 42.4 (Least nonunit divisor test). For a given natural input 𝑛≥2, the least divisor 𝑝of 𝑛satisfyin",
    "end": "e prime 𝑝, division gives a Boolean decision 𝑣𝑝(𝑥) for 𝑝∣𝑥. The two-factor result and the converse witness multiplication give 𝑣𝑝(𝑥𝑦) = 𝑣𝑝(𝑥) ∨2 𝑣𝑝(𝑦)"
  },
  {
    "volume": "V2",
    "version": "P2",
    "physical_page": "129",
    "chars": "1664",
    "extended_chars": "1664",
    "body_y0": "65.08",
    "body_y1": "651.94",
    "occupied_y_span": "586.86",
    "footer": "V2 / ReadFlow R1 / R7-P2 scoring draft | 120",
    "start": "on each stable source part. Moreover 𝑣𝑝(1) = f: an equation 1 = 𝑝𝑤with 𝑝≥2 is impos- sible on a noninitial par",
    "end": "ion on the counter 𝑖 constructs a state with four natural coordinates (𝑟0, 𝐶0, 𝑃0, 𝑈0) = (𝑛, 0, 1, 1), (𝑟, 𝐶, 𝑃, 𝑈) ⟼􏿴𝑣(𝑟), 𝐶+ 𝑝(𝑟)𝑈, 𝑃𝑝(𝑟), 𝐵𝑈􏿷. (F1)"
  },
  {
    "volume": "V2",
    "version": "P3",
    "physical_page": "133",
    "chars": "1392",
    "extended_chars": "1392",
    "body_y0": "68.64",
    "body_y1": "530.27",
    "occupied_y_span": "461.63",
    "footer": "V2 / ReadFlow R1 / R7-P3 scoring draft | 122",
    "start": "compositeness. The Boolean test below separates the source parts; no object of all properties is assumed. Prop",
    "end": "which these data apply, 𝑝∣𝑎or 𝑝∣𝑏on the appropriate stable parts. More generally, a prime dividing a given finite product divides at least one factor."
  },
  {
    "volume": "V2",
    "version": "P3",
    "physical_page": "134",
    "chars": "1557",
    "extended_chars": "1557",
    "body_y0": "68.56",
    "body_y1": "545.05",
    "occupied_y_span": "476.49",
    "footer": "V2 / ReadFlow R1 / R7-P3 scoring draft | 123",
    "start": "pf. Let 𝑔= 𝐺(𝑝, 𝑎). The gcd construction supplies 𝑔∣𝑝. On each represented factor- ization 𝑝= 𝑔𝑐, primality fo",
    "end": "ange and tests true, since it is 𝑟itself. The bounded-search theorem therefore gives a whole-source least index, not just local existential witnesses."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F07 · sentence split and isolated concluding tail

**volume**

V0

**source**

editorial_r7/004-03-reading-the-constructions.tex

**P3_lines**

104–127

**control**

L121: \enlargethispage{-5\baselineskip}; 6 earlier negative controls in same source

**quote_before**

It was the proposed shorter condition that lost information.

**quote_after**

PDF 42 ends “It was the proposed”; PDF 43 starts “shorter condition that lost information.” followed by one concluding paragraph.

**observation**

P3 43只有371字元、96.44pt文字跨度；不自然處包括句中斷與依賴上頁的句尾。P2 37結論在同頁。

**interpretation**

只禁止小於300字元的孤頁仍會漏掉。對讀者有意義的是句子和論證閉合，不是最低字元數。

**severity**

clear sentence-level regression

**source_sha256**

```json
{
  "P2": "ee0aa0ea52fe93fd44b97ab50dbb9dd783e1fb7a67c7794591f610b74debe380",
  "P3": "e17bc1d23334112c8928fa8cdf075e129f6aa8ad638d58bfad7258ff7b68c92a"
}
```

**page_records**

```json
[
  {
    "volume": "V0",
    "version": "P2",
    "physical_page": "37",
    "chars": "1366",
    "extended_chars": "1366",
    "body_y0": "68.64",
    "body_y1": "484.08",
    "occupied_y_span": "415.44",
    "footer": "V0 / ReadFlow R1 / R7-P2 scoring draft | 25",
    "start": "The first and last steps use associativity; the middle step substitutes the original com- patibility equation.",
    "end": "s equations, then com- pare candidates for that one test. The comparison used only the given pullback and arrows; no further construction was assumed."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "42",
    "chars": "1562",
    "extended_chars": "1562",
    "body_y0": "65.08",
    "body_y1": "566.86",
    "occupied_y_span": "501.78",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 27",
    "start": "A worked reading test. Fix a category and given arrows 𝑓∶𝐴→𝐶, 𝑔∶𝐵→𝐶 with a supplied pullback (𝑃, 𝑝, 𝑞), where ",
    "end": "ed 𝑤sending 𝑥to 1 has 𝑝∘𝑤= 𝛼∘𝑡but differs from 𝑢∘𝑡at 𝑥; it fails the required 𝑞equation. Uniqueness still holds for the full test. It was the proposed"
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "43",
    "chars": "371",
    "extended_chars": "371",
    "body_y0": "68.64",
    "body_y1": "165.07",
    "occupied_y_span": "96.44",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 28",
    "start": "shorter condition that lost information. This example connects types, substitution, supplied existence and fix",
    "end": "s equations, then com- pare candidates for that one test. The comparison used only the given pullback and arrows; no further construction was assumed."
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F08 · short-page negative control

**volume**

V2

**source**

layout/study/volume-2-study.tex

**P3_lines**

12

**control**

TOC baseline set to18pt

**quote_before**

End of table of contents.

**quote_after**

End of table of contents, five entries on P3 PDF 11.

**observation**

P3 11僅263字元，但屬目錄結束，不是證明或題目被任意拆散。

**interpretation**

不得只因短而列為數學閱讀缺陷；可另評目錄空間效率，沒有證據把它當造成68分的特定原因。

**severity**

no mathematical-continuity defect established

**source_sha256**

```json
{
  "P2": "3427267faa4c2d1cb9689e2a121f9e647b226b2de4f3f7f8c2a1a6f6e7327a09",
  "P3": "7b8c79f19cecc56e51b91db0da5c40a4eb6ff834a167a04f1e70e6c211aa4e12"
}
```

**page_records**

```json
[
  {
    "volume": "V2",
    "version": "P2",
    "physical_page": "9",
    "chars": "998",
    "extended_chars": "998",
    "body_y0": "69.21",
    "body_y1": "480.07",
    "occupied_y_span": "410.86",
    "footer": "V2 / ReadFlow R1 / R7-P2 scoring draft | viii",
    "start": "48 The ordered field of Cauchy values 177 48.1 Completion ring . . . . . . . . . . . . . . . . . . . . . . . .",
    "end": " . . . . . . . . . . . . . . . . . 208 From arithmetic to analysis: what the constructions deliver . . . . . . . . . . . . . . . 211 Working notes 212"
  },
  {
    "volume": "V2",
    "version": "P3",
    "physical_page": "11",
    "chars": "263",
    "extended_chars": "263",
    "body_y0": "69.36",
    "body_y1": "185.17",
    "occupied_y_span": "115.82",
    "footer": "V2 / ReadFlow R1 / R7-P3 scoring draft | x",
    "start": "51.2 Affine transport of bounds and separated sets . . . . . . . . . . . . . . . . . . 213 51.3 Rational cuts ",
    "end": " . . . . . . . . . . . . . . . . . 218 From arithmetic to analysis: what the constructions deliver . . . . . . . . . . . . . . . 221 Working notes 222"
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.

## F09 · definition split with local adjacency benefit

**volume**

V0

**source**

layout/views/v0/breadth/b07-path-categories.tex

**P3_lines**

23–50

**control**

L23: \enlargethispage{-3\baselineskip}

**quote_before**

For every supplied vertex $v$ there is also a length-zero path $\varepsilon_v$ from $v$ to $v$, with no edges.

**quote_after**

These two final lines of Definition1.15 are carried to a continued box on PDF53; positive-length paths remain on PDF52.

**observation**

P2 46同頁容納正長及零長路徑；P3 52/53拆開。但P3零長路徑與其必要tagging警語同頁，比P2的警語在47更接近。

**interpretation**

應以整個定義＋關鍵例外說明為閱讀單位考量。不得刪掉空路徑的端點標記以減短；不同頂點的空路徑必須區分。

**severity**

mixed outcome needing unit-level design

**source_sha256**

```json
{
  "P2": "d4edddb683623e05bfc2c696f7dd2c1c1b4a37d175fd14dda875e6a15e61b358",
  "P3": "3f3b30809be13ab85647a193cc3cfbf2a645afedf612b861011be2a5d91325a5"
}
```

**page_records**

```json
[
  {
    "volume": "V0",
    "version": "P2",
    "physical_page": "46",
    "chars": "1760",
    "extended_chars": "1760",
    "body_y0": "63.1",
    "body_y1": "665.48",
    "occupied_y_span": "602.39",
    "footer": "V0 / ReadFlow R1 / R7-P2 scoring draft | 34",
    "start": "Related reading F. W. Lawvere and R. Rosebrugh, Sets for Mathematics, Cambridge University Press, 2003, §1.1 (",
    "end": "𝑒2, … , 𝑒𝑛), 𝑠(𝑒1) = 𝑣, 𝑡(𝑒𝑛) = 𝑤, 𝑡(𝑒𝑖) = 𝑠(𝑒𝑖+1) (1 ≤𝑖< 𝑛). For every supplied vertex 𝑣there is also a length-zero path 𝜀𝑣from 𝑣to 𝑣, with no edges."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "52",
    "chars": "1687",
    "extended_chars": "1687",
    "body_y0": "63.1",
    "body_y1": "623.94",
    "occupied_y_span": "560.85",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 37",
    "start": "Related reading F. W. Lawvere and R. Rosebrugh, Sets for Mathematics, Cambridge University Press, 2003, §1.1 (",
    "end": "n different edges. A path of positive length from 𝑣to 𝑤is a supplied finite list 𝑝= (𝑒1, 𝑒2, … , 𝑒𝑛), 𝑠(𝑒1) = 𝑣, 𝑡(𝑒𝑛) = 𝑤, 𝑡(𝑒𝑖) = 𝑠(𝑒𝑖+1) (1 ≤𝑖< 𝑛)."
  },
  {
    "volume": "V0",
    "version": "P3",
    "physical_page": "53",
    "chars": "1635",
    "extended_chars": "1635",
    "body_y0": "65.2",
    "body_y1": "680.27",
    "occupied_y_span": "615.07",
    "footer": "V0 / ReadFlow R1 / R7-P3 scoring draft | 38",
    "start": "Definition 1.15 (continued) For every supplied vertex 𝑣there is also a length-zero path 𝜀𝑣from 𝑣to 𝑣, with no ",
    "end": " contain, in precisely this order, the edge occurrences of 𝑝, those of 𝑞, and those of 𝑟. Neither bracketing changes an edge or its position. Equality"
  }
]
```

**evidence_class**

actual source diff + PDF text + rendered visual inspection; diagnostic interpretation is not human scoring

**math_scope**

No full chapter/volume mathematical acceptance; examples retain source qualifications.
