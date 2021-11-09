import React from 'react';
import { useHistory } from 'react-router-dom';
import Layout from 'features/common/components/Layout';
import styled from "styled-components";

export default function UserDetail() {
    const detail = JSON.parse(localStorage.getItem('sessionUser'))
    const history = useHistory()
  return (
    <Layout><Main>
         <h1>회원정보</h1>
        <ul>
            <li>
                <label>
                    <span>회원번호 : {detail.userId} </span>
                </label>
            </li>
            <li>
                <label>
                    <span>아이디 : {detail.username} </span>
                </label>
            </li>
            <li>
                <label>
                <span>이메일 :  {detail.email}  </span>
                </label>
            </li>
            <li>
                <label>
                    <span>비밀 번호 :  *******  </span>
                </label>
            </li>
            <li>
                <label>
                <span>이름 : {detail.name} </span>
                </label>
            </li>
        </ul>
        <input type="button" value="회원정보수정" onClick={()=> history.push('/users/modify')}/>
    </Main></Layout>
  );
}
const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`