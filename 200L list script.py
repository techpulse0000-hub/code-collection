import pandas as pd


student_list = """1. Abdulganiyu Abdulmajeed Bidemi - 2024/1/97661EH

2. Jimoh Toibat Ometere - 2024/1/97748EH

3. Adam Musa Raji - 2024/1/96876EH

4. Ofor Emmanuel Chukwuma - 2024/1/96749EH

5. Okorie Victor Chidubem - 2024/1/97421EH

6. Damian Chidozie Daniel - 2024/1/98218/EH

7. Yakubu John Omoh - 2024/1/96759EH

8. Ezema Emmanuel Ifeanyichukwu - 2024/1/98125EH

9. Musa Raymond Aleakhue - 2024/1/95768EH

10. Akpera Fanen Japhet - 2024/1/98819EH

11. Jeff Success - 2024/1/97145EH

12. Omotosho Muhammad Monsur - 2024/1/97107EH

13. Adama Zainab - 2024/1/99537EH

14. Yunus Abdulraheem Ahmad - 2024/1/97197EH

15. Akpeji Divine Ewuoro - 2024/1/97279EH

16. Ojadeh Daniel Ojonimi - 2024/1/97973EH

17. Obetta Chiagozie Divine - 2024/1/96650EH

18. Lukman Muhammad - 2024/1/96975EH

19. Adebayo Oluwatunmise Adesola - 2024/1/101001EH

20. Isiaq Ridwanullahi Opeyemi - 2024/1/96138EH

21. Ezuma Paul Chukwuemeka - 2024/1/96133EH

22. Abdulkadri Kamaldeen - 2024/1/99240EH

23. Akuh Stephen - 2024/1/99664EH

24. Jerome Benjamin - 2024/1/97505EH

25. Victor Ozovehe Abraham - 2024/1/98306EH

26. Isah Samson Adejo - 2024/1/100930EH

27. Atonu Ahmed Ojodale - 2024/1/96582EH

28. Nworie Chinemerem Unique - 2024/1/98477EH

29. Adeyanju Martins Ayoade - 2024/1/98348EH

30. Okorie Victor Chima - 2024/1/98575EH

31. Daniel Omega - 2024/1/99127EH

32. Ahangba Terhemba Zachariah - 2024/1/98740EH

33. Adamu Firdausi Nana - 2024/1/98813EH

34. Aiyenale Olajesu Victory - 2024/1/97302EH

35. James Enoch Ayobami - 2024/1/96434EH

36. Okenwa Ekene Goodrich - 2024/1/97564EH

37. Olayinka Israel Oluwafunsho - 2024/1/97131EH

38. Adejoh Onuh - 2024/1/101121EH

39. Tiamiyu Mubarak Opeyemi - 2024/1/95964EH

40. Olatunde Janet Oluwabukunmi - 2024/1/97964EH

41. Adebisi Josephine Toluwalashe - 2024/1/100007EH

42. Babajide Ireoluwa David
        2024/1/97824EH

43. Olusola Abdulbasit Olanrewaju - 2024/1/97159EH

44. Bello Mariam Damilola - 2024/1/96340EH

45. Afolabi Faiz Olamilekan - 2024/1/97005EH

46. Udeh Chimezie Anslem - 2024/1/99259EH

47. Theophilus Oluwaseyi Adgebite - 2024/1/98871EH

48. Goldface Faithful - 2024/1/96723EH

49. Ogundele Afeez Ayomide - 2024/1/98432EH

50. Haruna Ismail Ibrahim - 2024/1/97341EH

51. Suleiman Jemilat Ozohu - 2024/1/98345EH

52. Asuquo Maobasi Bartholomew - 2024/1/96658EH

53. Enema Favour Ufedojo - 2024/1/99293EH

54. Otache Precious Ene - 2024/1/100885EH

55. Alade Miracle Rejoice - 2024/1/96774EH

56. Faruna Godboat - 2024/1/97111EH

57. Meeme Terpine Wilfred - 2024/1/96831EH

58. Adebayo David Oluwatimilehin - 2024/1/96762EH

59. Okwute Nemile - 2024/1/100705EH

60. Ezeude Obinna Francis - 2024/1/99656EH

61. Isaiah Goodness Somto - 2024/1/97129EH

62. Gidado Ibrahim Abdulsalam - 2024/1/99488EH

63. Ehiagwina Winnie Oisedebamen - 2024/1/95948EH

64. Onipe Benedict - 2024/1/98820EH

65. Abula Amarachi Miracle - 2024/1/96652EH

66. Christopher Daniel Saviour - 2024/1/96762EH

67. Okoh Micheal Ugochukwu - 2024/1/99201EH

68. Ogunleke Festus Ayodele - 2024/1/97547EH

69. Egwemi Hosiah - 2024/1/97188EH

70. Anthony Godwin Oshoma - 2024/1/97643EH

71. Yusuf Abdulkareem Olatunji - 2024/1/96931EH

72. Haruna Usman - 2024/1/98789EH

73. Mualim Muhammad Buhari - 2024/1/97531EH

74. AMEN ALHAMDU YAKUBU - 2024/1/99980EH

75. Oladejo Toyeeb Ajao - 2024/1/96970EH

76. Salako Musa Ajani - 2024/1/98418EH

77. Tochukwu Josephat Emeka - 2024/1/96952EH

78. Umar Sholagbade Olokodana - 2024/1/96494EH

79. Bello Kehinde Sharon - 2024/1/97141EH

80. Ofikhenua Anosi Benedict - 2024/1/95442EH

81. Odeyale Salahudeen Ajagbe - 2024/1/96737EH

82. Saidu Abdulmanan - 2024/1/97595EH

83. Kagbu Arigu James - 2024/1/97438EH

84. Adetoye Favour Elizabeth - 2024/1/100119EH

85. Oscar Victor Mosibgodi - 2024/1/97019EH

86. Mathew Majin Usman - 2024/1/98710EH

87. Adeyi Emmanuel Felix - 2024/1/100174EH

88. Hillary Harmony Ogbonna - 2024/1/98524EH

89. Saidu Abdulmanan - 2024/1/97595EH

90. Ogundele Precious Oluwatumininu - 2024/1/96718EH

91. Daniel Jedidiah Yitkinaan - 2024/1/100598EH

92. Yahaya Abubakar Kobo - 2024/1/97150EH

93. Babajide Ireoluwa David - 2024/1/97824EH

94. Esho Honour Fimisola - 2024/1/96648EH

95. Adeyemi Rebecca Folake - 2024/1/98879EH

96. Yakubu Mary - 2024/1/99562EH

97. Jude Samuel Chijioke - 2024/1/98052EH

98. Sule Olaniyi Lukman - 2024/1/101217EH

99. Agbo Gabriel Otanwa - 2024/1/96770EH

100. Makwe Celestine Emmanuel - 2024/1/101533EH

101. Enehe Adeiza - 2024/1/98174EH

102. Jibrin Ummulkhairi - 2024/1/97612EH

103. Ageh Christabel - 2024/1/97966EH

104. Amen Alhamdu Yakubu - 2024/1/99980EH

105. Moses Joseph Okpanachi - 2024/1/99414EH

106. Abwa Aondonenge Alfred - 2024/1/101228EH

107. Adams Emmanuel Edoh - 2024/1/97698EH

108. Eneche Eleojo Joy - 2024/1/97128EH

109. Akuhwa Michael - 2024/1/96923EH

110. Olayonu Daniel Oluwadamilola - 2024/1/97957EH

111. Christopher chibunnam Davies - 2024/1/99166EH

112. Noah Sophie Eniola - 2024/1/97051EH

113. Victor ozovehe Abraham - 2024/1/98306EH

114. Ibraheem Abdussalam ADEBAYO - 2023/1/94543EH

115. Aliyu Ayobami Precious - 2024/1/97623EH

116. Abass Kehinde Sheriffdeen - 2024/1/96677EH

117. Abula Amarachi Miracle - 2024/1/96652EH

118. Christabel Ekpe - 2024/1/97966EH

119. Oyome Emmanuel promise - 2023/1/89959EH

120. Christabel Ekpe - 2020/1/97966EH

121. Ubaha Faith Edet - 2025/2/105728EH

122. Maji uwodi - 2023/1/92187EH

123. Samuel Israel - 2024/1/98754EH
    
124. Chinedu Ifeanyi Bassy - 2023/1/90666EH

125. Abdulsalam lawal haruna - 2024/1/96880EH

126. Abdulhameed aliyu yusuf - 2024/1/98444EH

127. Saka halimat happiness - 2024/1/97274EH

128. ESHO HONOUR FIMISOLA - 2024/1/96648EH

129. Salawudeen Nurudeen omeiza - 2024/1/101291EH

130. Mohammed Mustapha - 2023/1/91972EH

131. Victor Abraham Ozovehe - 2024/1/98306EH

132. AMARI BENEDICT OGBADA - 2024/1/100777EH

133. Obetta Chiagozie Divine - 2024/1/96650EH

134. Enema Favour Ufedojo - 2024/1/99293EH

135. George Emmanuel - 2024/1/95633EH

136. Yakubu Mary - 2024/1/99562EH

137. UWADIAE OSAUME NATURAL - 2023/1/91893EH

138. Fortune Okudo Ifechukwu - 2023/1/90139EH

139. AKUHWA MICHAEL AGEBA - 2024/1/96923EH

140. IORNUMBE THOMAS - 2024/1/99121EH

141. Bello Abdulrahman - 2023/1/92413EH

142. Ibrahim Hafsat - 2024/1/97902EH

143. Adebisi Josephine toluwalashe - 2024/1/100007EH

144. Adams Emmanuel edoh - 2024/1/97698EH

145. Agbo Gabriel Otanwa - 2024/1/96770EH

146. Matthew Majin usman - 2024/1/98710EH

147. Alikali Mustapha - 2024/1/96982EH

148. Olayinka Israel oluwafunsho - 2024/1/97131EH

149. Akaazua Matthew Nater - 2024/1/101424EH

150. Abula Amarachi Miracle - 2024/1/96652EH

151. Christabel Ekpe - 2024/1/97966EH

152. Oyome Emmanuel promise - 2023/1/89959EH

153. Christabel Ekpe - 2024/1/97966EH

154. Ubaha Faith Edet - 2025/2/105728EH

155. Maji uwodi - 2023/1/92187EH

156. Okoh Micheal ugochukwu - 2024/1/99201EH

157. TIAMIYU ADELEKE KINGSLEY - 2024/1/101428EH

158. Abdulsalam lawal haruna - 2024/1/96880EH

159. Abdulhameed aliyu yusuf - 2024/1/98444EH

160. Saka halimat happiness - 2024/1/97274EH

161. ESHO HONOUR FIMISOLA - 2024/1/96648EH

162. Salawudeen Nurudeen omeiza - 2024/1/101291EH

163. Mohammed Mustapha - 2023/1/91972EH

164. Victor Abraham Ozovehe - 2024/1/98306EH

165. AMARI BENEDICT OGBADA - 2024/1/100777EH

166. Enema Favour Ufedojo - 2024/1/99293EH

167. George Emmanuel - 2024/1/95633EH

168. ABDUL SAMAD LIADI ADEYEMI - 2024/1/98350EH

169. Yakubu Mary - 2024/1/99562EH

170. UWADIAE OSAUME NATURAL - 2023/1/91893EH

171. Fortune Okudo Ifechukwu - 2023/1/90139EH

172. AKUHWA MICHAEL AGEBA - 2024/1/96923EH

173. IORNUMBE THOMAS - 2024/1/99121EH

174. Bello Abdulrahman - 2023/1/92413EH

175. Ibrahim Hafsat - 2024/1/97902EH

176. Adebisi Josephine toluwalashe - 2024/1/100007EH

177. Adams Emmanuel edoh - 2024/1/97698EH

178. Nabil Jubril - 2023/1/92240EH

179. Agbo Gabriel Otanwa - 2024/1/96770EH

180. Matthew Majin usman - 2024/1/98710EH

181. Alikali Mustapha - 2024/1/96982EH

182. Olayinka Israel oluwafunsho - 2024/1/97131EH

183. Akaazua Matthew Nater - 2024/1/101424EH

184. Yakubu John omoh - 2024/1/96759EH

185. Atonu Ahmed Ojodale - 2024/1/96582EH

186. Afolabi Femi Adura - 2024/1/96728EH

187. Mahmud Ibrahim Ahmad - 2025/2/108793EH

188. Isiah Goodness Somto - 2024/1/97129

189. Akpabio Idorenyin Uko - 2024/1/97256EH

190. Abwa Aondonenge Alfred - 2024/1/101228EH

191. Elesin jamiat omobukola - 2023/1/94247EH

192. Oladiti Precious Sarah - 2025/2/105026EH

193. Suleiman Muhammad - 2023/1/93600EH

194. Endurance Eromosele - 2023/1/93312EH

195. Sanyaolu victor Eromonsele 
2023/1/90613EH

196. Ogunbiyi Emmanuel Marvelous
2023/1/94322EH

197. Adikwu Paul Ochowupu 
2023/1/90639EH

198. Awwal adeiza husseni 
2023/1/93133EH

199. Ahmad ishaq abdulhammeed 
2023/1/93422EH"""






# for i in student_list.split("\n"):
 
updated_list = student_list.split("\n")
updated_list = [i.strip() for i in updated_list if i.strip() != ""]
# for i in updated_list:
#     if i.startswith("195. "):
#         i = i[3:]
#     print(i)


correction = updated_list[updated_list.index("195. Sanyaolu victor Eromonsele"):]
correction_1 = []
i = 0
j = 1
while True:
    

    c = correction[i]+correction[j]
    correction_1.append(c)
    i = j+1
    j = i+1

    if j == len(correction)-1:
        break

# print(correction)
# print(correction_1)
# print(updated_list.index("195. Sanyaolu victor Eromonsele"))
updated_list = updated_list[:updated_list.index("194. Endurance Eromosele - 2023/1/93312EH")]
updated_list = updated_list + correction_1
updated_list.append('199. Ahmad ishaq abdulhammeed - 2023/1/93422EH')

sn = []
name = []
matric = []
for i in updated_list:
    dot_idx = i.find(".")
    sn.append(i[:dot_idx].strip())
    remaining = i[dot_idx:]
    mat_idx = remaining.find("2")
    name.append(remaining[:mat_idx-1].strip().strip(".").strip("-").strip(" "))
    matric.append(remaining[mat_idx:].strip().strip(".").strip("-").strip(" "))


    

for k in name:
    sep_names = k.split()
    

# series = pd.DataFrame({"Name":name, "Matric. No":matric})
# ready_list = series.drop_duplicates()

# ready_list.to_csv("list of 200L 24/25 set", index=False)

# print(ready_list)

