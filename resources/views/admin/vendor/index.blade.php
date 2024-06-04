@extends('admin.layouts.app')

@section('content')
    <h1>Vendors</h1>
    <table class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Address</th>
                <th>Verified</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($vendors as $vendor)
                <tr>
                    <td>{{ $vendor->name }}</td>
                    <td>{{ $vendor->email }}</td>
                    <td>{{ $vendor->phone }}</td>
                    <td>{{ $vendor->address }}</td>
                    <td>{{ $vendor->verified? 'Yes' : 'No' }}</td>
                    <td>
                        <a href="{{ route('admin.vendors.show', $vendor->id) }}">View</a>
                        <a href="{{ route('admin.vendors.edit', $vendor->id) }}">Edit</a>
                        <a href="{{ route('admin.vendors.destroy', $vendor->id) }}">Delete</a>
                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>
@endsection
