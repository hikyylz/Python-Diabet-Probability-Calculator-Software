// go run GROUP_21_2020510074.go   şeklinde terminalde çalıştırabiliyorum.

package main

import (
	"encoding/csv"
	"fmt"
	"math"
	"os"
	"strconv"
)

// İki liste arasındaki Öklid mesafesini hesaplayan fonksiyon.
func euclideanDistance(list1, list2 []float64) {
	// Liste uzunluklarını kontrol et
	if len(list1) != 9 || len(list2) != 9 {
		fmt.Println("liste uzunluklari yanliş")
		return
	}

	// Diyabet sonuncu sonucunu kaldır (ilk 8 elemanı al)
	list1 = append(list1[:8])
	list2 = append(list2[:8])

	var calculationSum float64
	// Her iki listedeki karşılık gelen elemanların farkının karesini alıp topluyoruz.
	for i := 0; i < 8; i++ {
		subtraction := list1[i] - list2[i]
		power := math.Pow(subtraction, 2)
		calculationSum += power
	}

	// Hesaplanan toplamın karekökünü alarak Öklid mesafesini hesaplıyoruz.
	euclideanDistance := math.Sqrt(calculationSum)
	fmt.Println("--")
	fmt.Println("Seçilen noktalar arasindaki Öklid mesafesi")
	fmt.Println(euclideanDistance)
	fmt.Println("--")
}

// Programın ana fonksiyonu
func main() {
	// CSV dosyasının adını belirtiyoruz.
	csvFileName := "diabetes.csv"
	// İlgili satır numaralarını belirtiyoruz.
	dataRow1 := 1
	dataRow2 := 2

	// İki farklı liste oluşturuyoruz.
	var dataRow1List, dataRow2List []float64

	// CSV dosyasını aç
	csvFile, err := os.Open(csvFileName)
	if err != nil {
		fmt.Println("CSV dosyasini açarken hata oluştu:", err)
		return
	}
	defer csvFile.Close()

	// CSV dosyası için bir CSV okuyucu oluştur
	csvReader := csv.NewReader(csvFile)

	// CSV dosyasındaki sütun başlıklarını oku
	_, _ = csvReader.Read()

	// CSV dosyasını satır satır okuyup satır numarasını takip ediyoruz.
	rowCounter := 1
	for {
		data, _ := csvReader.Read()

		// Eğer satır numarası dataRow1'e eşitse, bu satırı ilgili listeye ekliyoruz.
		if rowCounter == dataRow1 {
			dataRow1List = parseCSVRow(data)
		}

		// Eğer satır numarası dataRow2'ye eşitse, bu satırı ilgili listeye ekliyoruz.
		if rowCounter == dataRow2 {
			dataRow2List = parseCSVRow(data)
		}

		// Eğer her iki liste de dolmuşsa, döngüyü kırıyoruz.
		if len(dataRow1List) != 0 && len(dataRow2List) != 0 {
			break
		}

		rowCounter++
	}

	// Öklid mesafesini hesapla
	euclideanDistance(dataRow1List, dataRow2List)
}

// Bir CSV satırını float64 tipinde bir listeye dönüştüren fonksiyon.
func parseCSVRow(row []string) []float64 {
	parsedRow := make([]float64, len(row))
	for i, val := range row {
		// Her elemanı float64 tipine dönüştürüp listeye ekliyoruz.
		floatVal, _ := strconv.ParseFloat(val, 64) // strconv go kütüphanesi, string to float casting yapmak isçin kullanıldı.
		parsedRow[i] = floatVal
	}
	return parsedRow
}
