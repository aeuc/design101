from openai import OpenAI

client = OpenAI(api_key='')

prompt = "[300 saat, Terzi, Cep Telefonu] = Normal Öncelikli,"
"[20 saat, Öğretmen, Cep Telefonu] = Düşük Öncelikli,"
"[10 saat, Doktor, Cep Telefonu] = Yüksek Öncelikli,"
"[600 saat, Tamirci, Cep Telefonu] = Yüksek Öncelikli,"
"[70 saat, Kurye, POS Cihazı] = Yüksek Öncelikli,"
"[10 saat, Dişçi, Mikrodalga] = Düşük Öncelikli"
" Yukarıdaki veriler şu şekildedir: Baz istasyonuna bağlı kalma süresi, Meslek, Bağlı cihaz. Uzun süre baz istasyonuna kalan insanlar yerel halk olduğundan dolayı öncelikleri var. Mesleklerin de kendi önemleri var, mesela bir doktor acil durumlarda ulaşılabilir olmalı, ama yerli olmayan bir öğretmen turist olacağından ötürü öncelik sırası düşük. Bağlı olan cihaz eğer çok önemli ve fazla insanı ilgilendiriyorsa öncelik sırası yüksek olmalı, POS cihazları ödeme yapmak için oldukça kritik."
"Baz istasyonunda yoğunluk varken öncelik sıralarına göre kullanıcılara kaynak dağılımı yapılması istenmektedir. Verilen bu örnek için yukarıdakileri değerlendirerek sadece kullanıcının önceliğini belirtir misin: "

bilgiler = input("Baz istasyonuna bağlantı süresi, Meslek, Bağlı Cihaz: ")


stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt + bilgiler}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")
