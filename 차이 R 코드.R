#t-test

setwd("D:/R")


rr1 <- read.csv("r_ttest.csv", fileEncoding="EUC-KR")
var.test(rr1$만족도 ~ rr1$성별1)
install.packages("lawstat")
library(lawstat)
levene.test(rr1$만족도,rr1$성별1,location="mean")


t.test(rr1$만족도 ~ rr1$성별1, var.equal=F)


#t-test 시각화
install.packages("gplots")
library(gplots)
plotmeans(rr1$만족도 ~ rr1$성별1, ci.label=T)


#대응표본 t-test

before <- c(66,51,69,74,100,63,86,90,69,83,75,72,98,69,67,88,55,56,74,57,56,76,71,85,76,78,62,60,67,67)
after  <- c(90,87,75,73,65,81,96,70,95,71,71,90,95,73,72,67,97,97,71,92,87,95,69,81,81,93,88,96,95,67)

diff=after-before
shapiro.test(diff)
t.test(before, after, paired=T)



##ANOVA

rr1 <- read.csv("r_anova.csv", fileEncoding="EUC-KR")
summary(rr1)

#등분산성 검정, 산업분야 --> 3개 이상의 수준이므로 var.test 대신 bartlett.test 사용
bartlett.test(rr1$만족도 ~ rr1$산업분야1)

ano1 <- aov(rr1$만족도 ~ rr1$산업분야1, data=rr1)
anova(ano1)
summary(ano1)

#gplot이외의 기본 패키지로 그림 그려 볼 것
#install.packages("gplots")
library(gplots)
plotmeans(rr1$만족도 ~ rr1$산업분야1, ci.label=T, mean.label=T)


#Duncan.test로 사후분석
install.packages("agricolae")
library(agricolae)
duncan.test(ano1, "rr1$산업분야", alpha=0.05, console=T)
              



rr2 <- subset(rr1,산업분야1=="제조업" | 산업분야1=="금융업")
rr3 <- subset(rr2,전공계열1=="공학계열" | 전공계열1=="사회계열" | 전공계열1=="인문계열")
  
bartlett.test(rr3$만족도 ~ rr3$산업분야1)
bartlett.test(rr3$만족도 ~ rr3$전공계열1)

ano2 <- aov(rr3$만족도 ~ rr3$산업분야1*rr3$전공계열1)
summary(ano2)

interaction.plot(rr3$산업분야1,rr3$전공계열1,rr3$만족도)

