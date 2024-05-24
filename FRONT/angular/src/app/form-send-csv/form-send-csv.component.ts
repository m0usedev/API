import { Component } from '@angular/core';
import { API_URL_UPLOAD_POST_CSV } from '../../utilities/api';

@Component({
  selector: 'app-form-send-csv',
  standalone: true,
  imports: [],
  templateUrl: './form-send-csv.component.html',
  styleUrl: './form-send-csv.component.css'
})
export class FormSendCsvComponent {
  state = 'select'

  stateUploadButton (state : string | any = undefined, response : object | string | any = undefined ) {
    /**
     * select - estado normal
     * upload - subiendose el archivo
     * error - cuando no se suvio el archivo, error en le servidor o
     */
    /**
     * respuestas:
     *  'bad', 'El fichero fue subido al servidor no es tipo .csv'
     *  'good', 'El fichero fue subido al servidor'
     * 'error', 'Ha surgido un error en el servidor'
     */
    if(response && response.response){
      let tipo = response.response
      switch (tipo) {
        case 'bad':
          this.state = 'error'
          alert(response.message)
          this.state = 'select'
          break;
        case 'good':
          this.state = 'select'
          alert(response.message)
          break;
        case 'error':
          this.state = 'error'
          alert(response.message)
          this.state = 'select'
          break;
        default:
          this.state = 'select'
          break;
      }
    }else{
      switch (state) {
        case 'select':
          this.state = 'select'
          alert(response)
          break;
        case 'upload':
          this.state = 'upload'
          break;
        case 'error':
          this.state = 'error'
          alert(response)
          this.state = 'select'
          break;
        default:
          this.state = 'select'
          break;
      }
    }
  }

  async onSubmit(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      if(input.files[0].type == 'text/csv'){
        const formData = new FormData();
        formData.append('file', input.files[0]);
        await this.fetchPostFile(formData);
        input.value = ''
      }else{
        input.value = ''
        this.stateUploadButton('error', 'El fichero debe ser de tipo csv')
      }
    } else {
      console.error('No has seleccionado ningun fichero');
      input.value = ''
      this.stateUploadButton('select', 'No has seleccionado ningun fichero')
    }
  }

  async fetchPostFile ( form : FormData ) {
    this.stateUploadButton('upload', undefined)
    fetch(
      API_URL_UPLOAD_POST_CSV,
      {
        method: "POST", // or 'PUT'
        body: form, // data can be `string` or {object}!
      }
    )
    .then( (response) => response.json() )
    .then( (data) => {
      if(data){
        this.stateUploadButton(undefined, data)
      }
    } )
  }
}
