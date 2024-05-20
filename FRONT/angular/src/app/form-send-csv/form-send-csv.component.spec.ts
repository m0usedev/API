import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormSendCsvComponent } from './form-send-csv.component';

describe('FormSendCsvComponent', () => {
  let component: FormSendCsvComponent;
  let fixture: ComponentFixture<FormSendCsvComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormSendCsvComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FormSendCsvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
