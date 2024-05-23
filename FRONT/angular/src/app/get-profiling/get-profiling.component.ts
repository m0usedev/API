import { Component } from '@angular/core';
import { API_URL_DOWNLOAD_GET_PROFILE } from '../../utilities/api';

@Component({
  selector: 'app-get-profiling',
  standalone: true,
  imports: [],
  templateUrl: './get-profiling.component.html',
  styleUrl: './get-profiling.component.css'
})
export class GetProfilingComponent {
  file_get_data = ''
  data : any
  colums_key : any

  responseData (blob : any, file : string) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = `${file}.html`;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
  }

  async fetchGetData(file: string) {
    try {
      const response = await fetch(API_URL_DOWNLOAD_GET_PROFILE + '?file=' + file, {
        method: "GET"
      });

      if (response.ok) {
        const contentType = response.headers.get('content-type');

        if (contentType && contentType.includes('application/json')) {
          const jsonData = await response.json();
          console.log('Error:', jsonData);
          alert(jsonData.error);
        } else {
          const blob = await response.blob();
          this.responseData(blob, file);
        }
      } else {
        console.error('Respuesta no ok:', response);
        alert('Error al descargar el archivo');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Hubo un problema con la solicitud');
    }
  }

}
