import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetProfilingComponent } from './get-profiling.component';

describe('GetProfilingComponent', () => {
  let component: GetProfilingComponent;
  let fixture: ComponentFixture<GetProfilingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GetProfilingComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(GetProfilingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
