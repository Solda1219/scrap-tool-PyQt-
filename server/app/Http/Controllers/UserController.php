<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use App\Models\Logintrack;
use App\Models\Package;
// use Illuminate\Support\Facades\DB;

class UserController extends Controller
{
    /**
     * Handle the incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function __invoke(Request $request)
    {
        //
    }

    public function register(Request $request)
    {

        $user = User::where('email', $request->input('email'))->first();
        if($user){
            return 'Email in use!';
        }
        else{
            try {
                if($request->input('role')){
                    // super part
                }
                else{
                    $user = new User;
                    $user->firstname = $request->input('firstname');
                    $user->lastname= $request->input('lastname');
                    $user->email= $request->input('email');
                    $user->password= md5($request->input('password'));
                    $user->role= 'user';
                    $user->save();
                    $queryStatus= "Register success!";
                }
                
            } catch(Exception $e){
                $queryStatus= "Error";
            }
            return $queryStatus;
        }
    }


    public function login(Request $request)
    {
        $user= User::where('email', $request->input('email'))->where('password', md5($request->input('password')))->first();
        $logintrack= new Logintrack;
        if($user){
            if(($user->loginstatus!= 'logedin') || ($user->ip== $request->input('ip')&& $user->uuid==$request->input('uuidCom'))){
                $user->loginstatus= "logedin";
                $user->ip= $request->input('ip');
                $user->uuid= $request->input('uuidCom');
                $user->save();

                $logintrack->email= $request->input('email');
                $logintrack->ip= $request->input('ip');
                $logintrack->uuid= $request->input('uuidCom');
                $logintrack->logininfo= 'Success';
                $logintrack->save();

                $packageId= $user->package_id;
                $package= Package::where('id', $packageId)->first();

                return response($package);
            }
            else {
                $logintrack->email= $request->input('email');
                $logintrack->ip= $request->input('ip');
                $logintrack->uuid= $request->input('uuidCom');
                $logintrack->logininfo= 'Attempt failed';
                $logintrack->save();

                return "already logedin";
            }
        }
        else{
            return "invalid user";
        }
    }
    public function logout(Request $request)
    {
        $user= User::where('email', $request->input('email'))->first();
        if($user){
            $user->loginstatus= '';
            $user->save();
            return 'logout success';
        }
        else{
            return "something went wrong";
        }
    }
    public function alertLoginStatus(Request $request)
    {
        
    }
}
