maasAyse = 5000
maasArzu = 4000
vergi = 0.27

print(maasAyse- (maasAyse * vergi))
print(maasArzu- (maasArzu * vergi))

# Değişken Tanımlama Kuralları

# Rakam ile başlayamaz

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanmamalıyız

yas = 20
_age = 20

x = 1              #init
y = 2.3            #stole
name = "Aysun"     #string
isStudent = True   #bool

x, y, name, isStudent = (1, 2.3, "Aysun", True )

a = "10"
b = "20"
print=(a+b) # => 1020

firstName = "Zeynep"
lastName = " Turan"

print(firstName + lastName)  # Zeynep Turan

