import Image from 'next/image'

const Logo = () => {
    return (
        <div className="flex items-center justify-center gap-3">
            <Image 
                width={50}
                height={50}
                src={'/icon-512.png'}
            />
            <h1 className="text-white font-bold text-2xl"> Smarteach </h1>
        </div>
    );
}

export default Logo;