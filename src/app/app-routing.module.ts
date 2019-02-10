import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { LendingClubComponent } from './lending-club/lending-club.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'api/json', component: LendingClubComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
