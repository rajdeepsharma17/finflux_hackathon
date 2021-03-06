import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LendingClubComponent } from './lending-club/lending-club.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ClarityModule } from '@clr/angular';
import { LoginComponent } from './login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    LendingClubComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ClarityModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
