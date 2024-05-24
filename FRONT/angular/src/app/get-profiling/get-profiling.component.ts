import { Component } from '@angular/core'
import { API_URL_DOWNLOAD_GET_PROFILE } from '../../utilities/api'
interface User {
  "file"      : Blob,
  "file_name" : string
}
@Component({
  selector: 'app-get-profiling',
  standalone: true,
  imports: [],
  templateUrl: './get-profiling.component.html',
  styleUrl: './get-profiling.component.css'
})
export class GetProfilingComponent {
  file_get_data  : string
  visible        : false | true
  stateProfiling : false | true
  file_download  : User

  constructor() {
    this.file_get_data  = ''
    this.visible        = false
    this.stateProfiling = false
    this.file_download  = {
      "file"      : new Blob(),
      "file_name" : ''
    }
  }

  renderHtml(blob: Blob) {
    const reader = new FileReader()
    reader.onload = (event) => {
        const contentFrame = document.getElementById('contentFrame') as HTMLIFrameElement;
        if (contentFrame && contentFrame.contentDocument && event.target) {
            const result = event.target.result;
            if (typeof result === 'string') {
                const doc = contentFrame.contentDocument;
                doc.open();
                doc.write(result);
                doc.close();
                this.visible = true
                this.stateProfiling = false
            }
        }
    };
    reader.readAsText(blob);
  }

  downbload() {
    let blob = this.file_download.file
    let file_name = this.file_download.file_name
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.style.display = 'none'
    a.href = url
    a.download = `${file_name}.html`
    document.body.appendChild(a)
    a.click()
    window.URL.revokeObjectURL(url)
  }

  async fetchGetData(file_name: string) {
    this.visible = false
    this.stateProfiling = true
    try {
      const response = await fetch(API_URL_DOWNLOAD_GET_PROFILE + '?file_name=' + file_name, {
        method: "GET"
      })

      if (response.ok) {
        const contentType = response.headers.get('content-type')

        if (contentType && contentType.includes('application/json')) {
          const jsonData = await response.json()
          if(jsonData.response )
            this.stateProfiling = false
            alert(jsonData.message)
        } else {
          const blob = await response.blob()
          this.renderHtml(blob)
          this.file_download.file = blob
          this.file_download.file_name = file_name
        }
      } else {
        console.error('Respuesta no ok:', response)
        alert('Error al descargar el archivo')
      }
    } catch (error) {
      console.error('Error:', error)
      alert('Hubo un problema con la solicitud')
    }
  }

}
