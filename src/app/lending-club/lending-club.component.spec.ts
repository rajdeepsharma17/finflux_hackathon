import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LendingClubComponent } from './lending-club.component';

describe('LendingClubComponent', () => {
  let component: LendingClubComponent;
  let fixture: ComponentFixture<LendingClubComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LendingClubComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LendingClubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
