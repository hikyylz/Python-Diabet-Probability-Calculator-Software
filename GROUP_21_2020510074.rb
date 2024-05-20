
# ruby GROUP_21_2020510074.rb  şeklinde terminalde çalıştırabiliyorum.

require 'csv'

def euclidean_distanceM(list1, list2)
  # Liste doğruluğunu kontrol et
  if list1.length != 9 || list2.length != 9
    puts "Liste uzunlukları yanlış"
    return
  end

  # Diyabet sonucunu kaldır
  list1.pop
  list2.pop

  calculation_sum = 0
  (0..7).each do |i|
    subtraction = list1[i] - list2[i]
    power = subtraction ** 2
    calculation_sum += power
  end

  euclidean_distance = Math.sqrt(calculation_sum)
  puts "--"
  puts "Seçilen noktalar arasındaki Öklid mesafesi"
  puts euclidean_distance
  puts "--"
end

csv_file_name = "diabetes_preprocessed.csv"
data_row1 = 3
data_row2 = 77


data_row1_list = []
data_row2_list = []


# CSV dosyasını aç ve satır satır oku
CSV.foreach(csv_file_name, headers: true).with_index(1) do |row, row_index|
  if row_index == data_row1
    data_row1_list = row.fields.map(&:to_f)
    break if data_row2_list.any?
  end
  if row_index == data_row2
    data_row2_list = row.fields.map(&:to_f)
    break if data_row1_list.any?
  end
end


# Öklid mesafesini hesapla
euclidean_distanceM(data_row1_list, data_row2_list)
