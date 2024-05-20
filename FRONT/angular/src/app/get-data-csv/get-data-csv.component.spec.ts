import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetDataCsvComponent } from './get-data-csv.component';

describe('GetDataCsvComponent', () => {
  let component: GetDataCsvComponent;
  let fixture: ComponentFixture<GetDataCsvComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GetDataCsvComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(GetDataCsvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
