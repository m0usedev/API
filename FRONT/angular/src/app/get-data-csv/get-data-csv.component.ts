import { Component } from '@angular/core';
import { API_URL_GET_FILE_CSV_DATA } from '../../utilities/api';

@Component({
  selector: 'app-get-data-csv',
  standalone: true,
  imports: [],
  templateUrl: './get-data-csv.component.html',
  styleUrl: './get-data-csv.component.css'
})
export class GetDataCsvComponent {
  file_get_data = ''
  data : any
  colums_key : any

  responseData (data : any) {
    this.data = data
    this.colums_key = Object.keys(data.table)
  }

  async fetchGetData ( file : string ) {
    fetch(
      API_URL_GET_FILE_CSV_DATA+'?file='+file,
      {
        method: "GET", // or 'PUT'
      }
    )
    .then( (response) => response.json() )
    .then( (data) => this.responseData(data)  )
  }

}
