# Polski podział administracyjny
Repozytorium powstało ze względu na to, że nie znalazłem na internecie podobnego zbioru danych, wykonałem go za pomocą autorskich skryptów i w oparciu o dane [Głównego Urzędu Statystycznego](https://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default)

### Miasta
 - ID
 - nazwę
 - nazwę unikalną (bez polskich znaków), w przypadku miejscowości powtarzających się jest ona unikalna poprzez dokładanie losowych 5 cyfr po znaku `"unique_name": "dobra_35525"`
 - przyporządkowanie do powiatu po ID
 - przyporządkowanie do województwa po ID
 - wysokość i szerokość geograficzną (latitude)
 
### Powiaty
 - ID
 - nazwę
 - przyporządkowanie do województwa po ID

### Województwa
- ID
- nazwę
- nazwę unikalną bez polskich znaków

Zbiór danych sformatowany został w UTF-8

## Przykładowe wykorzystanie
Odległość pomiędzy miastami

Javascript:
```javascript
 function calcCrow(lat1, lon1, lat2, lon2) 
    {
	  
      var R = 6371; // km, m=6371000 itp.
      var dLat = toRad(lat2-lat1);
      var dLon = toRad(lon2-lon1);
      var lat1 = toRad(lat1);
      var lat2 = toRad(lat2);

      var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2); 
      var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
      var d = R * c;
      return d;
    }

    function toRad(Value) 
    {
        return Value * Math.PI / 180;
    }
```
PHP:
```php
function calcCrow($lat1, $lon1, $lat2, $lon2){
        $R = 6371; // km, m=6371000 itp.
        $dLat = toRad($lat2-$lat1);
        $dLon = toRad($lon2-$lon1);
        $lat1 = toRad($lat1);
        $lat2 = toRad($lat2);

        $a = sin($dLat/2) * sin($dLat/2) +sin($dLon/2) * sin($dLon/2) * cos($lat1) * cos($lat2); 
        $c = 2 * atan2(sqrt($a), sqrt(1-$a)); 
        $d = $R * $c;
        return $d;
}

function toRad($Value) 
{
    return $Value * pi() / 180;
}
```


## Licencja
[MIT](https://choosealicense.com/licenses/mit/) - prawo do używania, kopiowania, modyfikowania i rozpowszechniania
