import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { list } from 'features/user/reducer/userSlice'
const UserListForm = () => {
    
    const dispatch = useDispatch()

    const users = useSelector(state => state.user.usersState);
    const type = useSelector(state => state.user.type)
    const keyword = useSelector( state => state.user.keyword)
    const page = 1;
    
    useEffect(() => {
      const param = {type: type, keyword: keyword, page: page}
      dispatch(list(param))
    },[]);

    return (<table border='1px' style={{textAlign:'center'}}>
    <thead>
    <tr><th>사용자번호</th>
        <th>사용자아이디</th>
        <th>이름</th>
        <th>이메일</th></tr>
    </thead>
    <tbody>
        {users.map((i, userId) => (
            <tr key={userId}><td>{i.userId}</td>
            <td>{i.username}</td>
            <td>{i.name}</td>
            <td>{i.email}</td></tr>
        ))}
    
    </tbody>
    </table>)
}

export default UserListForm