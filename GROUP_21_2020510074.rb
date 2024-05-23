
# ruby GROUP_21_2020510074.rb  şeklinde terminalde çalıştırabiliyorum.
require 'csv'

# İki liste arasındaki Öklid mesafesini hesaplayan fonksiyon.
def euclidean_distanceM(list1, list2)
  # Liste uzunluklarını kontrol et
  if list1.length != 9 || list2.length != 9
    puts "Liste uzunlukları yanlış"
    return
  end

  # Diyabet sonucunu kaldır (son elemanı çıkar)
  list1.pop
  list2.pop

  # Hesaplama için toplam değişkeni
  calculation_sum = 0

  # Her iki listedeki karşılık gelen elemanların farkının karesini alıp topluyoruz.
  (0..7).each do |i|
    subtraction = list1[i] - list2[i]
    power = subtraction ** 2
    calculation_sum += power
  end

  # Hesaplanan toplamın karekökünü alarak Öklid mesafesini hesaplıyoruz.
  euclidean_distance = Math.sqrt(calculation_sum)
  puts "--"
  puts "Seçilen noktalar arasındaki Öklid mesafesi"
  puts euclidean_distance
  puts "--"
end

# CSV dosyasının adını belirtiyoruz.
csv_file_name = "diabetes.csv"
# İlgili satır numaralarını belirtiyoruz.
data_row1 = 1
data_row2 = 2
# İki farklı liste oluşturuyoruz.
data_row1_list = []
data_row2_list = []

# CSV dosyasını aç ve satır satır oku
CSV.foreach(csv_file_name, headers: true).with_index(1) do |row, row_index|
  # Eğer satır numarası data_row1'e eşitse, bu satırı ilgili listeye ekliyoruz.
  if row_index == data_row1

    # Seçili row içerisindeki verileri float a çevirip data_row1_list'e atıyoruz.
    data_row1_list = row.fields.map(&:to_f)
    # Diğer liste de dolmuşsa döngüyü kır
    break if data_row2_list.any?
  end
  # Eğer satır numarası data_row2'ye eşitse, bu satırı ilgili listeye ekliyoruz.
  if row_index == data_row2
    
    # Seçili row içerisindeki verileri float a çevirip data_row2_list'e atıyoruz.
    data_row2_list = row.fields.map(&:to_f)
    # Diğer liste de dolmuşsa döngüyü kır
    break if data_row1_list.any?
  end
end

# Öklid mesafesini hesapla
euclidean_distanceM(data_row1_list, data_row2_list)
