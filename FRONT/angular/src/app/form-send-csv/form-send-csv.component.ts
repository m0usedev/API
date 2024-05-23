import { Component } from '@angular/core';
import { API_URL_POST_FILE_CSV } from '../../utilities/api';

@Component({
  selector: 'app-form-send-csv',
  standalone: true,
  imports: [],
  templateUrl: './form-send-csv.component.html',
  styleUrl: './form-send-csv.component.css'
})
export class FormSendCsvComponent {

  async onSubmit(event: Event) {
    const input = event.target as HTMLInputElement;

    if (input.files && input.files.length > 0) {
      if(input.files[0].type == 'text/csv'){
        const formData = new FormData();
        formData.append('file', input.files[0]);
        await this.fetchPostFile(formData);
      }else{
        console.log('El fichero debe ser de tipo csv')
      }
    } else {
      console.error('No has seleccionado ningun fichero');
    }
  }


  async fetchPostFile ( form : FormData ) {
    fetch(
      API_URL_POST_FILE_CSV,
      {
        method: "POST", // or 'PUT'
        body: form, // data can be `string` or {object}!
      }
    )
    .then( (response) => response.json() )
    .then( (data) => console.log(data) )
  }
}
