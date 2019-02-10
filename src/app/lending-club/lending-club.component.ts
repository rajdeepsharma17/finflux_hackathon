import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-lending-club',
  templateUrl: './lending-club.component.html',
  styleUrls: ['./lending-club.component.css']
})


export class LendingClubComponent implements OnInit {
  
  members = []
  constructor(private http: HttpClient) { }

  ngOnInit() {
    if(this.members.length == 0)
    this.showConfig()
  }

  getConfig() {
    return this.http.get('http://0.0.0.0:5000/api/json');
  }


  showConfig() {
    console.log("called")
    this.getConfig()
      .subscribe((result: any) => {
        for(let member of result.Members){
          this.members.push(member)
        }
      });
  }

}
