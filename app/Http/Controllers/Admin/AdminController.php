namespace App\Http\Controllers\Admin;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Models\User;
use App\Models\Product;

class AdminController extends Controller
{
    public function dashboard()
    {
        $users = User::all();
        $products = Product::all();
        return view('admin.dashboard', compact('users', 'products'));
    }

    public function users()
    {
        $users = User::all();
        return view('admin.users', compact('users'));
    }

    public function products()
    {
        $products = Product::all();
        return view('admin.products', compact('products'));
    }
}
