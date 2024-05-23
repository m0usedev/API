import { Component, ComponentFactoryResolver } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { API_URL_GET, API_URL_POST } from '../utilities/api';

import { FormSendCsvComponent } from './form-send-csv/form-send-csv.component';
import { GetDataCsvComponent } from './get-data-csv/get-data-csv.component';
import { GetProfilingComponent } from './get-profiling/get-profiling.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    FormSendCsvComponent,
    GetDataCsvComponent,
    GetProfilingComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  async fetchGet ( texto : string) {
    fetch( API_URL_GET+texto )
      .then( (response) => response.json() )
      .then( (data) => console.log(data) )
  }

  async fetchPost ( texto : string) {
    var data = {"name": texto}

    fetch(
      API_URL_POST,
      {
        method: "POST", // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
    .then( (response) => response.json() )
    .then( (data) => console.log(data) )
  }

}
