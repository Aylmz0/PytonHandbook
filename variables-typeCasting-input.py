#noktalı virgüle gerek yok
print("pepperoni")

#değişkenler için int falan yazmaya gerek yok
name = "Abdullah"
print(name)

#değişken yazdırma işi f olmadan olmaz
age=20
print(f"I am {age} years old ")

#int str dönüşümü
newAge = str(age)
newAge += "1"
print(newAge)

#Java scaner benzeri, klavyeden input alıcak.
# Yazılan kelime hemen cümlenin yanına yazılıyor ama
#İnput sonucu yazan şey String kabul edilir. Dönüştürülmesi gerekebilir
age = int(input("how old are you?"))
