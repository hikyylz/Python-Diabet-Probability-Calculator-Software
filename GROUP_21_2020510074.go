// go run GROUP_21_2020510074.go   şeklinde terminalde çalıştırabiliyorum.

package main

import (
	"encoding/csv"
	"fmt"
	"math"
	"os"
	"strconv"
)

func euclideanDistance(list1, list2 []float64) float64 {
	// Liste doğruluğunu kontrol et
	if len(list1) != 9 || len(list2) != 9 {
		fmt.Println("liste uzunluklari yanliş")
		return 0
	}

	// Diyabet sonuncu sonucunu kaldır
	list1 = append(list1[:8])
	list2 = append(list2[:8])

	var calculationSum float64
	for i := 0; i < 8; i++ {
		subtraction := list1[i] - list2[i]
		power := math.Pow(subtraction, 2)
		calculationSum += power
	}

	euclideanDistance := math.Sqrt(calculationSum)
	fmt.Println("--")
	fmt.Println("Seçilen noktalar arasindaki Öklid mesafesi")
	fmt.Println(euclideanDistance)
	fmt.Println("--")

	return euclideanDistance
}

func main() {
	csvFileName := "diabetes_preprocessed.csv"
	dataRow1 := 1
	dataRow2 := 2

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
	_, err = csvReader.Read()
	if err != nil {
		fmt.Println("CSV başliklarini okurken hata oluştu:", err)
		return
	}

	// İki örnek veriyi seç
	rowCounter := 1
	for {
		data, err := csvReader.Read()
		if err != nil {
			fmt.Println("CSV satirini okurken hata oluştu:", err)
			break
		}

		if rowCounter == dataRow1 {
			dataRow1List = parseCSVRow(data)
		}

		if rowCounter == dataRow2 {
			dataRow2List = parseCSVRow(data)
		}

		if len(dataRow1List) != 0 && len(dataRow2List) != 0 {
			break
		}

		rowCounter++
	}

	// Öklid mesafesini hesapla
	euclideanDistance(dataRow1List, dataRow2List)
}

func parseCSVRow(row []string) []float64 {
	var parsedRow []float64
	for _, val := range row {
		floatVal, err := strconv.ParseFloat(val, 64)
		if err != nil {
			fmt.Println("CSV satirini dönüştürürken hata oluştu:", err)
			return nil
		}
		parsedRow = append(parsedRow, floatVal)
	}
	return parsedRow
}
