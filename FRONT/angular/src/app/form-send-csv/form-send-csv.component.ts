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

  selectedFile: File | null = null

  onFileChange(event: Event) {
    const input = event.target as HTMLInputElement
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  async onSubmit(event: Event) {
    event.preventDefault()
    if (this.selectedFile) {
      const formData = new FormData()
      formData.append('file', this.selectedFile)
      await this.fetchPostFile(formData)
    } else {
      console.error('No file selected')
    }
  }

  async fetchPostFile ( form : FormData ) {
    console.log("pepe")
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
